# file rename tool
# text files can be found at /Users/aleks/Documents/_GIthub_Repositories/micro_projects/File_rename_tool/test_files
# or relative File_rename_tool/test_files
import os

test_path = "/Users/aleks/Documents/_GIthub_Repositories/micro_projects/File_rename_tool/test_files"


def rename(path, new_name):
    """
    Renames all files in the given path that end with ".txt" to the new name provided.

    Args:
    - path (str): The path to the directory containing the files to be renamed.
    - new_name (str): The new name to be used for the files.
    """
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

while True:
    print("Enter 'q' to quit")
    print("Enter 'r' to rename")
    user_input = input("Enter your choice: ")
    if user_input == "q":
        break
    elif user_input == "r":
        new_file_name = input("Enter new file name: ").strip()
        while new_file_name == "":
            new_file_name = input("Enter new file name: ")

        file_path = input("Enter file path: ").strip()
        if file_path == "test":
            file_path = test_path
        while os.listdir(file_path) == []:
            print("No files in directory")
            file_path = input("Enter file path: ").strip()
        rename(test_path, new_file_name)
    else:
        print("Invalid input")
