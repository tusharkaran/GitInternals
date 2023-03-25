import os
import hashlib
import shelve
from constants import INDEX_PATH


def isSha(path):
    with open(path , 'rb') as file:
        file_Data= file.read()
        file_hash = hashlib.sha256(file_Data).hexdigest
        return file_hash
    

    
def getshafromindex(filepath):
    with shelve.open(INDEX_PATH) as index:
        try:
            return index[filepath]
        except KeyError:
            return

        
