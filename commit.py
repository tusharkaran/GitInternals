import os
from commit_tree import commmit_tree
from constants import OBJ_PATH ,BASE_PATH ,HEAD_PATH
import hashlib
import pickle
import zlib


def commit(message):
    commmit_tree()
    commmit_object(message)



def commmit_object(message):
    tree_hash = "334343jjj3nri4i34icdvdvvvdv"
    dict ={
        "hash":tree_hash,
        "author_name":"username@git.com",
        "commiter_name":"Xyz",
        "commit_message":message
    }
    data_head = open(HEAD_PATH , "r").read()
    object_head_file = open(os.path.join(OBJ_PATH , data_head) , 'rb').read()
    if object_head_file != "":
        dict["parent_tree"] = data_head
    
    data = pickle.dumps(dict)
    sha = hashlib.sha256(data).hexdigest()
    compressed_commit = zlib.compress( data, zlib.Z_BEST_COMPRESSION)
    commit_object_file = open(os.path.join(OBJ_PATH , sha) , "wb").write(compressed_commit)
    head_file_last_commit_sha = open(HEAD_PATH , "w").write(sha)
    print(dict)

 
