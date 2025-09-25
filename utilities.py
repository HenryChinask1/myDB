# utilities.py
import os

def validate(path:str, file:str) -> bool:
    '''Check if a file exists.'''

    fileName = os.path.join(path, file)
    if os.path.exists(fileName):
        return True
    return False