import os
import utility
import shelve
from constants import BASE_PATH,INDEX_PATH,OBJ_PATH

def stage(file_path ,modified):
    file_stage = utility.intial(file_path ,os.stat(file_path) ,modified)
    print("stage self" ,file_stage, INDEX_PATH)

    with shelve.open(INDEX_PATH) as index:
        index[file_path] = file_stage
    
        





def add(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file != '.base':
               add(os.path.join(path,file))
    else:
        try:
            # entry_sha = utility.getshafromindex(path)
            sha_file = utility.isSha(path)
            # modified = entry_sha != sha_file
            modified = True
            stage(path , modified)
            # if not modified:   
            #     return
        except:
            pass
        
        
        




