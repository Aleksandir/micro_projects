# file rename tool
# text files can be found at /Users/aleks/Documents/_GIthub_Repositories/micro_projects/File_rename_tool/test_files
# or relative File_rename_tool/test_files
import os

test_path = "/Users/aleks/Documents/_GIthub_Repositories/micro_projects/File_rename_tool/test_files"


def rename(path, new_name):
    # Create a variable to track the number of files
    count = 0
    # Loop over each file in the path
    for file in os.listdir(path):
        # Check if the file ends with ".txt"
        if file.endswith(".txt"):
            # Increment the file count by 1
            count += 1
            # Create a new file name using the count variable
            new_file_name = f"{new_name}{count}.txt"
            # Create the old file path using the os.path.join() method
            old_file_path = os.path.join(path, file)
            # Create the new file path using the os.path.join() method
            new_file_path = os.path.join(path, new_file_name)
            # Rename the file using the os.rename() method
            os.rename(old_file_path, new_file_path)


rename(test_path, "hello")
