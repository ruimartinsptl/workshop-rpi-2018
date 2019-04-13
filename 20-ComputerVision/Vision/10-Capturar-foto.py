#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
__author__ = 'Rui Martins'

import os
import cv2
import time
import datetime
video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()
# timename = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S')
# frame_id = 1
# cv2.imwrite(os.path.join( "f-" + timename + "-" + '%0*d' % (5, frame_id) + ".png"), frame)
cv2.imwrite(os.path.join("imagem-usb.png"), frame)
video_capture.release()
cv2.destroyAllWindows()


# Em JUPYTER usar plt.imshow em vez de cv2.imshow
# display the image on screen and wait for a keypress
# cv2.imshow("Image", frame)
# cv2.waitKey(0)

import matplotlib.pyplot as plt
plt.imshow(frame)
plt.show()