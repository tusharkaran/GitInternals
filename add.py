import os
import utility
from constants import BASE_PATH,INDEX_PATH,OBJ_PATH
def add(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file != '.base':
               add(os.path.join(path,file))
    else:
        try:
            sha_file = utility.isSha(path)
            print(path , sha_file)
        except:
            pass




