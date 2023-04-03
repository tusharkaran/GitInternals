import os
import utility

def init(base):
    try:
        base_dir = os.path.join(base, '.base')
        obj_dir = os.path.join(base_dir, 'objects')
        refs_dir = os.path.join(base_dir, 'refs')
        head_path = os.path.join(base_dir, 'head')

        os.mkdir(base_dir)
        os.mkdir(obj_dir)
        os.mkdir(refs_dir)

        with open(head_path, "w") as head:
            head.write("main")
    except FileExistsError:
        pass
