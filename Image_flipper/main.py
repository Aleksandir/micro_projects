# Tutorial https://www.youtube.com/watch?v=kq9hmaNK5ZM

# test image path
# python3 main.py --image /Users/aleks/Documents/_GIthub_Repositories/micro_projects/Image_flipper/Duck_image.jpg

import argparse

import cv2


def main():
    """
    This script reads an image file and displays it, then applies a horizontal flip to the image and displays the result.
    The path to the image file is passed as a command line argument.

    Example usage:
    python main.py --image /path/to/image.jpg
    """
    # construct the argument parser and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to the image")
    arg = vars(parser.parse_args())

    image = cv2.imread(arg["image"])
    cv2.imshow("Original", image)
    cv2.waitKey(0)

    horizontal_flip = cv2.flip(image, 1)
    cv2.imshow("Horizontal Flip", horizontal_flip)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
