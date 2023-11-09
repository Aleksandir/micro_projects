import os

import cv2

IMAGE_EXTENSIONS = [".jpeg", ".png", ".jpg"]


def mirror_image(directory):
    """
    Reads an image from the specified file path, mirrors it horizontally, and saves the mirrored image to a new file with the
    '_mirror' suffix appended to the original filename.

    Args:
        filepath (str): The path to the image file to be mirrored.

    Returns:
        int: The number of images that were mirrored.
    """
    files = os.listdir(directory)

    # Loop through the files and mirror any that end with an image extension
    count = 0
    for file in files:
        if file.endswith(tuple(IMAGE_EXTENSIONS)):
            # Read the image
            image = cv2.imread(os.path.join(directory, file))

            # Mirror the image horizontally
            mirrored_image = cv2.flip(image, 1)

            # Save the mirrored image with the '_mirror' suffix appended to the original filename
            mirrored_filename = (
                os.path.splitext(file)[0] + "_mirror" + os.path.splitext(file)[1]
            )
            cv2.imwrite(os.path.join(directory, mirrored_filename), mirrored_image)

            count += 1
    return count


def delete_rotated_images(directory):
    """
    Deletes all rotated images in the specified directory.

    Args:
        directory (str): The directory to search for rotated images.

    Returns:
        int: The number of rotated images that were deleted.
    """
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Loop through the files and delete any that end with _mirror and have an image file extension
    count = 0
    for file in files:
        if file.endswith(tuple(IMAGE_EXTENSIONS)) and file.endswith(
            "_mirror" + os.path.splitext(file)[1]
        ):
            os.remove(os.path.join(directory, file))
            count += 1
    return count


def get_input(prompt, valid_inputs):
    response = input(prompt)
    while response not in valid_inputs:
        response = input(prompt)
    return response


def get_path(prompt):
    path = input(prompt)
    while not os.path.isdir(path):
        path = input(prompt)
    return path


path = ""
while True:
    print("1. Delete mirrored images")
    print("2. Mirror images in a directory")
    print("3. Exit")

    option = get_input("Enter an option: ", ["1", "2", "3"])

    if option == "3":
        break

    if path == "":
        path = get_path("Enter a path: ")
    else:
        print(f"Current path: {path}")
        if get_input("Change path? (y/n): ", ["y", "n"]) == "y":
            path = get_path("Enter a path: ")

    match option:
        case "1":
            count = delete_rotated_images(path)
            print(f"Deleted {count} images.")

        case "2":
            count = mirror_image(path)
            print(f"Mirrored {count} images.")
