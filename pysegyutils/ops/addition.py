import os 
import segyio 

from ..core import SegyFile, SegyFileAttributes, is_segy_valid 

def add(input_filepath_list, output_filepath, average=False, 
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

    pass 
