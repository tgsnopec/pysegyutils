import os
import segyio 
import numpy as np 

def is_segy_valid(segy_file_path, iline=9, xline=21):
    """
    """
    try:
        segy_file = segyio.open(segy_file_path, 'r',
                                    ignore_geometry=True,
                                    strict=False,
                                    iline=iline, 
                                    xline=xline)
        
        ilines = segy_file.attributes(iline)[:]
        xlines = segy_file.attributes(xline)[:]

        assert len(ilines) == segy_file.tracecount, 'Cannot read inline data from the file'
        assert len(ilines) == len(xlines), 'File seems malformed'
        assert segy_file.tracecount > 0, 'No traces in the SEG-Y file'

        segy_file.close()
    except:
        return False 
    
    return True 

class SegyFileAttributes(object):
    """
    """
    def __init__(self, segy_file_path, mode='r', iline=9, xline=21):

        segy_file = segyio.open(segy_file_path, 'r',
                                ignore_geometry=True,
                                strict=False,
                                iline=iline, xline=xline)

        self.ilines = segy_file.attributes(iline)[:]
        self.xlines = segy_file.attributes(xline)[:]
        self.tracecount = segy_file.tracecount
        self.samples = segy_file.samples 

        segy_file.close()
    
    def __eq__(self, other):
        """
        """
        equality_conditions = [self.tracecount == other.tracecount, 
                               np.all(self.ilines == other.ilines), 
                               np.all(self.xlines == other.xlines), 
                               np.all(self.samples == other.samples)]
        
        if all(equality_conditions) == True:
           return True 

        return False

class SegyFile(object):

    def __init__(self, segy_file_path, mode='r', iline=9, xline=21):
        
        self.segy_file = segyio.open(segy_file_path, mode=mode,
                                     ignore_geometry=True,
                                     strict=False,
                                     iline=iline, xline=xline)
        self.mode = mode 

    def __neg__(self):
        """
        """
        try:
            for it in range(self.segy_file.tracecount):
                self.segy_file.trace[it] *= -1
        except OSError as o:
            # TODO: Raise this better
            raise o 
        except Exception as e: 
            # TODO: Raise 
            raise e 
    
    def close(self):
        self.segy_file.close()
