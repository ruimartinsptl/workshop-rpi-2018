# import the necessary packages
import numpy as np
#import urllib
import cv2
import os

path = "./imagem-net.png"

image = cv2.imread(path)
print(type(image))

# Em JUPYTER usar plt.imshow em vez de cv2.imshow
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
