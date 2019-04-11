# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and grab each channel: Red, Green, and Blue. It's
# important to note that OpenCV stores an image as NumPy array with
# its channels in reverse order! When we call cv2.split, we are
# actually getting the channels as Blue, Green, Red!
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

# merge the image back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# visualize each channel in color
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)


# QUIZ:
cv2.imshow("QUIZ: Original", image)
(b, g, r) = cv2.merge([zeros, zeros, R])[94, 180]  # x=180, y=94 (as coordenadas estao trocadas)
print "Pixel at (94, 180) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
(b, g, r) = cv2.merge([B, zeros, zeros])[78, 13]  # (as coordenadas estao trocadas)
print "Pixel at (78, 13) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
(b, g, r) = cv2.merge([zeros, G, zeros])[5, 80]  # (as coordenadas estao trocadas)
print "Pixel at (5, 80) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)
cv2.waitKey(0)
