import os
import utility

def init(base):
    try:
        base_dir = os.path.join(base, '.base')
        obj_dir = os.path.join(base_dir, 'objects')
        stage_dir = os.path.join(base_dir, 'index')
        os.mkdir(base_dir)
        os.mkdir(obj_dir)
        os.mkdir(stage_dir)
        
        


    except FileExistsError:
        pass
