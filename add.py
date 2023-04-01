import os
import utility
import shelve
from constants import BASE_PATH,STAGE_PATH,OBJ_PATH

def stage(file_path ,modified):
    file_stage = utility.intial(file_path ,os.stat(file_path) ,modified)
    utility.compress_file_by_path(file_path)
    with shelve.open(STAGE_PATH) as index:
        index[file_path] = file_stage



def add(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file != '.base':
               add(os.path.join(path,file))
    else:
        try:
            entry_sha = utility.getshafromindex(path)
            sha_file = utility.isSha(path)
            utility.decompress_file_by_path(sha_file)
            modified = entry_sha != sha_file
            if not modified:   
                return
        except:
            pass
        stage(path , modified)
        modified = False
        
        




