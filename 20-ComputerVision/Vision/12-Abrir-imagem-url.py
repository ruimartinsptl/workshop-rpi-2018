#!/usr/bin/env python3

# import the necessary packages
import numpy as np
import urllib
import cv2
import os

url = "https://cbsnews1.cbsistatic.com/hub/i/2016/12/14/4b7e3037-b62b-4f21-9e5c-1c181da45a6a/screen-shot-2016-12-14-at-4-25-12-pm.png"
url = "https://upload.wikimedia.org/wikipedia/en/f/ff/SuccessKid.jpg"

import sys
if sys.version_info[0] == 3:
    from urllib.request import urlopen
elif sys.version_info[0] == 2:
    from urllib import urlopen
resp = urlopen(url)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

# Em JUPYTER usar plt.imshow em vez de cv2.imshow
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()

# Salvar imagem no disco
cv2.imwrite(os.path.join("imagem-net.png"), image)
cv2.destroyAllWindows()
