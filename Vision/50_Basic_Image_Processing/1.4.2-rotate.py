# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
 
# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

# rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
 
# rotate our image by -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

# rotate our image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((cX - 50, cY - 50), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Offset & 45 Degrees", rotated)

# finally, let's use our helper function in imutils to rotate the image by
# 180 degrees (flipping it upside down)
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

# QUIZ
rotated = imutils.rotate(image, -30)
cv2.imshow("Rotated by -30 Degrees [clockwise]", rotated)
(b, g, r) = rotated[254, 335]
print "Pixel at (y=254, x=335) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
print
rotated = imutils.rotate(image, 110)
cv2.imshow("Rotated by 110 Degrees [counter-clockwise]", rotated)
(b, g, r) = rotated[136, 312]
print "Pixel at (y=136, x=312) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
print
M = cv2.getRotationMatrix2D((50, 50), 88, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Offset & 88 Degrees", rotated)
(b, g, r) = rotated[10, 10]
print "Pixel at (y=10, x=10) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
cv2.waitKey(0)


# ######################################################################################################################
# imutils.py
# ######################################################################################################################
# def rotate(image, angle, center=None, scale=1.0):
#     # grab the dimensions of the image
#     (h, w) = image.shape[:2]
#
#     # if the center is None, initialize it as the center of
#     # the image
#     if center is None:
#         center = (w / 2, h / 2)
#
#     # perform the rotation
#     M = cv2.getRotationMatrix2D(center, angle, scale)
#     rotated = cv2.warpAffine(image, M, (w, h))
#
#     # return the rotated image
#     return rotated
# ######################################################################################################################