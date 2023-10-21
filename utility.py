import os
import hashlib
import shelve
import zlib
import pickle
from constants import STAGE_PATH ,OBJ_PATH

class intial:
    def __init__(self , file_path  ,stat ,modified):
        self.file_path = file_path
        self.sha = isSha(file_path)
        self.stat = stat
        self.modified = modified



def compress_file_by_path(path):
    hash = isSha(path)
    data = open(path, 'rb').read()
    compressed_data = zlib.compress( data, zlib.Z_BEST_COMPRESSION)
    f = open(os.path.join(OBJ_PATH ,hash) , "wb")
    f.write(compressed_data)
    f.close
    return



def decompress_file_by_path(hash):
    data = open(os.path.join(OBJ_PATH ,hash), 'rb').read()
    decompress_data = zlib.decompress(data)
    return decompress_data



def isSha(path):
    with open(path , 'rb') as file:
        file_Data= file.read()
        file_hash = hashlib.sha256(file_Data).hexdigest()
        return file_hash



def getshafromindex(filepath):
    with shelve.open(STAGE_PATH) as index:
        try:
            sha = index[filepath].sha
            return sha
        except KeyError:
            return

        
def get_modified_entry():
    modified_entry = []
    with shelve.open(STAGE_PATH) as index:
        try:
            for key in index.keys():
                entry = index[key]
                if entry.modified:
                    modified_entry.append(entry)
        except KeyError:
            return
    return modified_entry    


def compress_tree(dic):
    data = pickle.dumps(dic)
    hash = hashlib.sha256(data).hexdigest()
    c_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    f = open(os.path.join(OBJ_PATH, hash), 'wb')
    f.write(c_data)
    f.close()
    # perm = oct(os.stat(os.path.join(OBJ_DIR, hash)).st_mode)[2:]
    # fname = os.path.basename(os.path.join(OBJ_DIR, hash))
    # dic = {}
    # dic['filename'] = fname
    # dic['permissions'] = perm
    # dic['sha256'] = hash
    return hash