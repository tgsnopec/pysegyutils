import segyio 

from ..core import is_segy_valid, SegyFile
from ..core.file_copy_utils import fast_copy

def negate_file(input_file, output_file, iline=9, xline=21):
    """
    Negate a given SEG-Y file
    """
    if not is_segy_valid(input_file):
        error_message = f'Refusing to continue as the {input_file} is not SEG-Y.'
        raise RuntimeError(error_message)

    try:
        fast_copy(input_file, output_file)
    except OSError as o:
        # TODO
        raise o 

    output_segy_file = segyio.open(output_file, mode='r+', ignore_geometry=True,
                                   strict=False, iline=iline, xline=xline)

    for it in range(output_segy_file.tracecount):
        output_segy_file.trace[it] *= -1
    
    output_segy_file.close()
