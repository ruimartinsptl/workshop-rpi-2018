# import the necessary packages
import argparse
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, grab its dimensions, and show it
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
# cv2.imshow("Original", image) # DESCOMENTAR QUEM TIVER ACESSO SSH -X
cv2.imwrite(os.path.join("30-Original.png"), image)

# images are just NumPy arrays. The top-left pixel can be found at (0, 0)
(b, g, r) = image[225, 111]
print "Pixel at (y=225, x=111) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

# now, let's change the value of the pixel at (0, 0) and make it red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print "Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b)

# compute the center of the image, which is simply the width and height
# divided by two
(cX, cY) = (w / 2, h / 2)

# since we are using NumPy arrays, we can apply slicing and grab large chunks
# of the image -- let's grab the top-left corner
tl = image[0:cY, 0:cX]  # extract the [0, cX) and [0, cY) region of the image
# cv2.imshow("Top-Left Corner", tl) # DESCOMENTAR QUEM TIVER ACESSO SSH -X
cv2.imwrite(os.path.join("30-Top-Left.png"), tl)

# in a similar fashion, let's grab the top-right, bottom-right, and bottom-left
# corners and dispaly them
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
# cv2.imshow("Top-Right Corner", tr)# DESCOMENTAR QUEM TIVER ACESSO SSH -X
cv2.imwrite(os.path.join("30-Top-Right.png"), tr)
# cv2.imshow("Bottom-Right Corner", br)# DESCOMENTAR QUEM TIVER ACESSO SSH -X
cv2.imwrite(os.path.join("30-Bottom-Right.png"), br)
# cv2.imshow("Bottom-Left Corner", bl)# DESCOMENTAR QUEM TIVER ACESSO SSH -X
cv2.imwrite(os.path.join("30-Bottom-Left.png"), bl)

# now let's make the top-left corner of the original image green
image[0:cY, 0:cX] = (0, 255, 0)

# Show our updated image
# cv2.imshow("Updated", image) # DESCOMENTAR QUEM TIVER ACESSO SSH -X
cv2.imwrite(os.path.join("30-Updated.png"), image)
# cv2.waitKey(0) # DESCOMENTAR QUEM TIVER ACESSO SSH -X
