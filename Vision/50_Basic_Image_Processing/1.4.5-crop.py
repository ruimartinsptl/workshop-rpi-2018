# import the necessary packages
import cv2
 
# load the image and show it
image = cv2.imread("../images/florida_trip.png")
cv2.imshow("Original", image)
 
# cropping an image is accomplished using simple NumPy array slices --
# let's crop the face from the image
face = image[85:250, 85:220]
cv2.imshow("Face", face)
cv2.waitKey(0)
 
# ...and now let's crop the entire body
body = image[90:450, 0:290]
cv2.imshow("Body", body)
cv2.waitKey(0)

# QUIZ

a = image[124:212, 225:380]
cv2.imshow("a", a)
b = image[173:235, 13:81]
cv2.imshow("b", b)
c = image[85:250, 85:220]
cv2.imshow("c", c)
d = image[90:450, 0:290]
cv2.imshow("d", d)

e = image[124:212, 225:380]
cv2.imshow("e", e)
f = image[173:235, 13:81]
cv2.imshow("f", f)
g = image[85:250, 85:220]
cv2.imshow("g", g)
h = image[90:450, 0:290]
cv2.imshow("h", h)

cv2.waitKey(0)
