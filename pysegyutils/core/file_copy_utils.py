import sys 
import os 
import shutil 

def fast_copy(source, destination):
    """
    """
    try:
        shutil.copyfile(source, destination)
    except:
        shutil.copyfileobj(source, destination)