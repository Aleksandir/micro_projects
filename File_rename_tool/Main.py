# file rename tool
# text files can be found at /Users/aleks/Documents/_GIthub_Repositories/micro_projects/File_rename_tool/test_files
# or relative File_rename_tool/test_files
import os

test_path = "/Users/aleks/Documents/_GIthub_Repositories/micro_projects/File_rename_tool/test_files"


def rename(path, new_name):
    for file in os.listdir(path):
        if file.endswith(".txt"):
            os.rename(os.path.join(path, file), os.path.join(path, new_name + file))
        else:
            continue
        # rest of your code


rename(test_path, "t")
