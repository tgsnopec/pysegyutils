import os 
import numpy as np
import segyio 

from ..core import SegyFile, SegyFileAttributes, is_segy_valid 
from ..core.file_copy_utils import fast_copy

def add_files(input_filepath_list, output_filepath, average=False, 
              iline=9, xline=21):
    """
    Add two or more SEG-Y files
    """
    if all([is_segy_valid(entry) for entry in input_filepath_list]) == False:
        error_message = 'Unable to perform add operation as not all files are SEG-Y.'
        raise RuntimeError(error_message)

    input_attributes = [SegyFileAttributes(entry, iline=iline, xline=xline) 
                        for entry in input_filepath_list]

    if not (input_attributes[1:] == input_attributes[:-1]):
        error_message = 'Unable to add files as the geometry of all the files '
        error_message += 'is not the same.'
        raise RuntimeError(error_message)

    # Copy the first file to an output file to prevent writing the entire file
    try:
        fast_copy(input_filepath_list[0], output_filepath)
    except OSError as o:
        # TODO: Use this error message to print something more meaningful 
        error_message = f'Unable to create output file at {output_filepath}'
        raise o 

    # Open and store the input files in a list
    input_segy_files = []
    for entry in input_filepath_list:
        segy_file = segyio.open(entry, ignore_geometry=True, strict=False,
                                       iline=iline, xline=xline)
        input_segy_files.append(segy_file)

    # Open the output file too
    output_segy_file = segyio.open(output_filepath, 'r+', ignore_geometry=True,
                                   strict=False, iline=iline, xline=xline)

    factor = 1.0

    if average:
        factor = 1.0 / float(len(input_segy_files))

    for it in range(input_segy_files[0].tracecount):
        sum_trace = np.zeros_like(input_segy_files[0].trace[it])
        for entry in input_segy_files:
            sum_trace += entry.trace[it]
        
        output_segy_file.trace[it] = factor * sum_trace 
    
    # Cleanup now - close all the input files
    for entry in input_segy_files:
        try:
            entry.close()
        except:
            continue 
    
    # Close output file too
    output_segy_file.close()
