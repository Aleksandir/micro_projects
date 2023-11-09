import os

import cv2

IMAGE_EXTENSIONS = [".jpeg", ".png", ".jpg"]


def mirror_image(filepath):
    # Read the image
    img = cv2.imread(filepath)

    # Mirror the image
    mirrored_img = cv2.flip(img, 1)

    # Get the filename and extension of the original image
    filename, ext = os.path.splitext(filepath)

    # Construct the new filename with the _mirror suffix
    new_filename = f"{filename}_mirror{ext}"

    # Save the mirrored image
    cv2.imwrite(new_filename, mirrored_img)


def delete_rotated_images(directory):
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


while True:
    print("1. Delete mirrored images")
    print("2. Mirror images in a directory")
    print("3. Exit")

    option = input("Enter an option: ")
    while option not in ["1", "2", "3"]:
        option = input("Enter an option: ")

    path = input("Enter a path: ")
    while not os.path.isdir(path):
        path = input("Enter a path: ")

    match option:
        case "1":
            count = delete_rotated_images(path)
            print(f"Deleted {count} images.")

        case "2":
            count = 0
            for image in os.listdir(path):
                if image.endswith(tuple(IMAGE_EXTENSIONS)):
                    mirror_image(os.path.join(path, image))
                    count += 1
            print(f"Mirrored {count} images.")

        case "3":
            break
