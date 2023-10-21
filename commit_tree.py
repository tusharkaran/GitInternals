import os
import utility
from constants import STAGE_PATH ,OBJ_PATH ,temp


def commmit_tree():
    added_value = get_staged_tree()
    if not added_value:
        print('Nothing to commit')
        return
    return new_commit_tree(added_value)

    

def get_staged_tree() -> dict:
    modified_file_data = utility.get_modified_entry()
    if len(modified_file_data) == 0:
        return
    staged_tree = dict()
    common_object = {"files": None, "dirs": None}
    root_dir_name = ''
    staged_tree[root_dir_name] = {**common_object}
    for entry in modified_file_data:
        file_path_parts = os.path.normpath(entry.file_path).split(os.sep)
        file_path_parts = file_path_parts[1:]
        curr_dir = staged_tree[root_dir_name]
        for parts in file_path_parts[:-1]:
            if not curr_dir['dirs']:
                curr_dir['dirs'] = dict()
            if parts not in curr_dir['dirs']:
                curr_dir['dirs'][parts] = {**common_object}
            curr_dir = curr_dir["dirs"][parts]
    if not curr_dir["files"]:
        curr_dir["files"] = dict()
    curr_dir["files"][file_path_parts[-1]] = entry

    print("get_staged_tree ", staged_tree)
    return staged_tree

    
def new_commit_tree(staged_files):
    tree_name = ''
    # tree_name = os.path.split(CWD)[1]
    # print(tree_name)
    return new_commit_tree_helper(staged_files[tree_name], tree_name)

def new_commit_tree_helper(staged_files: dict, tree_path: str) -> str:
    tree = dict()
    tree["name"] = os.path.split(tree_path)[1]
    tree_entries = list()
    if staged_files["dirs"]:
        for entry in staged_files["dirs"].keys():
            tree_obj = dict()
            tree_obj["sha"] = new_commit_tree_helper(
                staged_files["dirs"][entry], os.path.join(tree_path, entry)
            )
            tree_obj["type"] = "tree"
            #static permission 
            tree_obj["mode"] ="556567"
            tree_obj["name"] = entry

            tree_entries.append(tree_obj)

    if staged_files["files"]:
        for entry in staged_files["files"].keys():
            blob_obj = dict()
            blob_obj["name"] = entry
            blob_obj["sha"] = staged_files["files"][entry].sha
            blob_obj["mode"] = staged_files["files"][entry].stat.st_mode
            blob_obj["type"] = "blob"
            tree_entries.append(blob_obj)

    tree["entries"] = tree_entries

    return utility.compress_tree(tree)









