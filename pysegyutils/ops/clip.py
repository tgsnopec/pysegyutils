import os 
import numpy as np 
import segyio 

from ..core import SegyFile, is_segy_valid
from ..core.file_copy_utils import fast_copy

def clip_as(input_file, grid_source_file, output_filepath,
            iline=9, xline=21):
    """Clip a given file according a specified grid.

       Only traces within the specified grid file will 
       be kept. The rest of the traces will be discarded.

    Args:
        input_file ([type]): [description]
        grid_source_file ([type]): [description]
        output_filepath ([type]): [description]
        iline (int, optional): [description]. Defaults to 9.
        xline (int, optional): [description]. Defaults to 21.
    """
    if not is_segy_valid(input_file):
        msg = f'File: {input_file} cannot be read as SEG-Y'
        raise RuntimeError(msg)
    
    if not is_segy_valid(grid_source_file):
        msg = f'File: {grid_source_file} cannot be read as SEG-Y'
        raise RuntimeError(msg)
    
    try:
        fast_copy(grid_source_file, output_filepath)
    except OSError as o:
        raise o 

    in_segy_file = segyio.open(input_file, 'r', ignore_geometry=True, 
                               strict=False, iline=iline, xline=xline)
    
    # Copy text header and binary header from the input file and zero traces
    out_segy_file = segyio.open(output_filepath, 'r+', ignore_geometry=True, 
                                strict=False, iline=iline, xline=xline)
    
    out_segy_file.text[0] = in_segy_file.text[0]
    out_segy_file.bin = in_segy_file.bin

    for it in range(out_segy_file.tracecount):
        out_segy_file.trace[it] = np.zeros_like(out_segy_file.trace[0])
    
    out_segy_file.close()

    # Create a dictionary to look up traces by inline and crossline in the input file
    trace_dict = dict()
    in_segy_ilines = in_segy_file.attributes(iline)[:]
    in_segy_xlines = in_segy_file.attributes(xline)[:]

    for it, (il, xl) in enumerate(zip(in_segy_ilines, in_segy_xlines)):
        trace_dict[il, xl] = it 
    
    # Start looking up the traces from out_segy_file now
    out_segy_file = segyio.open(output_filepath, 'r+', ignore_geometry=True, 
                                strict=False, iline=iline, xline=xline)
    
    out_segy_ilines = out_segy_file.attributes(iline)[:]
    out_segy_xlines = out_segy_file.attributes(xline)[:]

    for it, (il, xl) in enumerate(zip(out_segy_ilines, out_segy_xlines)):
        try:
            in_trace = trace_dict[il, xl]
            out_segy_file.trace[it] = in_segy_file.trace[in_trace]
        except KeyError:
            continue 
    
    out_segy_file.close()






