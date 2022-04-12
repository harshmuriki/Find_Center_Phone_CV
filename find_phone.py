import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys


def classifier(image):
    """ Method to use the trained Haar Classifier cascade-98.xml and apply it on the image
        And output the image (cropped image which consists only the phone) and input it into the.
        find_center method and get the coordinates outputed by it and return them.

    Args:
        image (numpy ndarray): The image given in the termnal.

    Returns:
        tuple: The (x,y) coordinates of the position of the center of the phone.
    """

    # image = cv2.imread("find_phone/1.jpg")
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    stop_data = cv2.CascadeClassifier(
        "cascade-98.xml"
    )

    found = stop_data.detectMultiScale(img_rgb, minSize=(24, 24))

    amount_found = len(found)

    if amount_found != 0:

        for (x, y, width, height) in found:

            imgNew = img_gray[y: y + height, x: x + width]

            y_c, x_c = find_center(imgNew)

            # print("y_c:", y_c, x_c)

        return ((x + x_c) / (image.shape[1]), (y + y_c) / (image.shape[0]))

    else:
        imgNew = img_gray
        y_c, x_c = find_center(imgNew)
        return (x_c / (image.shape[1]), y_c / (image.shape[0]))


def find_center(image):
    """ Method to find the center of the image using adaptive thresholding.
        The image is inputed from the Method classifier.
        Returns the coordinates of the center of the phone in the image.

    Args:
        image (numpy ndarray): The original or the cropped image of the phone.

    Returns:
        tuple: The (x,y) coordinates of the phone (the image cropped from the Method classifier).
    """

    blur = cv2.GaussianBlur(image, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 25
    )

    mass_x, mass_y = np.where(thresh == 0)
    cent_h = (np.average(mass_x)).astype(int)
    cent_w = (np.average(mass_y)).astype(int)

    return (cent_w, cent_h)


# Get the file name from the terminal and save to variable filename.
filename = sys.argv[1]
image = cv2.imread(str(filename))
x, y = classifier(image)

# The final (x,y) coordinates of the center of the phone in the given image.
x_coordinate = (round(x, 4))
y_coordinate = (round(y, 4))

print(x_coordinate, y_coordinate)
