import cv2
import numpy as np
import os
import sys
import fnmatch


def sharpen(image):
    """[sharpen image ]

    Args:
        image ([string]): [image name]

    Returns:
        [new_image]: [new sharpen image]
    """
    kernal = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    new_image = cv2.filter2D(image, -1, kernal)
    cv2.imshow('sharpened', new_image)
    cv2.waitKey(0)
    return new_image


def blur_image(image):
    """[blur image]

    Args:
        image ([string]): [image name]
    """
    kernels = [3, 5, 9, 13]
    for idx, k in enumerate(kernels):
        image_bl = cv2.blur(image, ksize=(k, k))
        cv2.imshow(str(k), image_bl)  # image show
        cv2.waitKey(0)  # stop
    return


def resize(fname, width, height):
    """
    Image Processing with Python opencv-python

    Args:
        fname ([string]): [image name ]
        width ([integer]): [new width for image]
        height ([integer]): [new width for image]

    Returns:
        [fname]: [image name]
        [new_image]: [new i,age with new size]

    """
    image = cv2.imread(fname)  # read priginal image
    cv2.imshow('Original Image', image)  # show original image
    cv2.waitKey(0)  # stop

    org_height, org_width = image.shape[0:2]  # original width and height

    # print width and height
    print("width", org_width)
    print("height", org_height)

    # check image height and width and resize to new size
    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))

    return fname, new_image


listOfFiles = os.listdir('.')
pattern = "*.jpg"
n = len(sys.argv)
if n == 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    width = 1280
    height = 960

if not os.path.exists('new_folder'):
    os.makedirs('new_folder')


for filename in listOfFiles:
    if fnmatch.fnmatch(filename, pattern):
        filename, new_image = resize(filename, width, height)
        cv2.imwrite('new_folder\\'+filename, new_image)

# filename,new_image=resize('image (1).jpg',200,200)

# cv2.imshow('resized image',new_image)
# cv2.waitKey(0)
# blur_image(new_image)

# sharpen(new_image)
