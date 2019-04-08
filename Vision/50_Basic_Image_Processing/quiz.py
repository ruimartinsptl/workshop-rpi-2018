__author__ = 'Rui Martins'

# import the necessary packages
import numpy as np
import imutils
import cv2

# load the image and show it
image = cv2.imread("../images/wynn.png")
cv2.imshow("Original", image)

# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

# rotate our image by ? degrees
M = cv2.getRotationMatrix2D((cX, cY), -30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -30 Degrees", rotated)

(b, g, r) = rotated[254, 335]
print "Pixel at (335, 254) in rotated - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)


# rotate our image by ? degrees
M = cv2.getRotationMatrix2D((cX, cY), 110, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 110 Degrees", rotated)

(b, g, r) = rotated[136, 312]
print "Pixel at (312, 136) in rotated - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)


# rotate our image by ? degrees
M = cv2.getRotationMatrix2D((50, 50), 88, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 88 Degrees", rotated)

(b, g, r) = rotated[10, 10]
print "Pixel at (10, 10) in rotated - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

cv2.waitKey(0)