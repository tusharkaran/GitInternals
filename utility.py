import os
import hashlib
import shelve
from constants import INDEX_PATH

class intial:
    def __init__(self , file_path  ,stat ,modified):
        self.file_path = file_path
        self.sha = isSha(file_path)
        self.stat = stat
        
        
        


def isSha(path):
    with open(path , 'rb') as file:
        file_Data= file.read()
        file_hash = hashlib.sha256(file_Data).hexdigest()
        return file_hash
    

    
# def getshafromindex(filepath):
#     with shelve.open(INDEX_PATH) as index:
#         try:
#             sha = index[filepath].sha
#             return sha
#         except KeyError:
#             return

        
