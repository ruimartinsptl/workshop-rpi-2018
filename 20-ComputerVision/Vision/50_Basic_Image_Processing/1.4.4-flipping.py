# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

# QUIZ:
# flip the image horizontally
flipped = cv2.flip(image, 1)

# grab the dimensions of the image and calculate the center of the image
(h, w) = flipped.shape[:2]
(cX, cY) = (w / 2, h / 2)

# rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(flipped, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

(b, g, r) = flipped[189, 441]  # x=441, y=189
print "Pixel at (189, 441) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
cv2.waitKey(0)

# QUIZ
import imutils
# flip the image vertically
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped horizontally", flipped)

(b, g, r) = flipped[235, 259]  # x=235, y=259
print "Pixel at (235, 259) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
cv2.waitKey(0)

rotated = imutils.rotate(flipped, 45)
cv2.imshow("Rotated by 45 Degrees [counter-clockwise]", rotated)
flipped = cv2.flip(rotated, 0)
cv2.imshow("Flipped vertically", flipped)
(b, g, r) = flipped[189, 441]
print "Pixel at (189, 441) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
