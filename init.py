import os
import utility

def init(base):
    try:
        base_dir = os.path.join(base, '.base')
        obj_dir = os.path.join(base_dir, 'objects')
        os.mkdir(base_dir)
        os.mkdir(obj_dir)
    except FileExistsError:
        pass
