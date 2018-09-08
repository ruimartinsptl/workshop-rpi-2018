#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
__author__ = 'Rui Martins'

import cv2

# load the image and show some basic information on it
image = cv2.imread('Imagem1.png')   # returns a NumPy array representing the image
print "width: %d pixels" % (image.shape[1])
print "height: %d pixels" % (image.shape[0])
print "channels: %d" % (image.shape[2])

# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# save the image -- OpenCV handles converting filetypes
# automatically
cv2.imwrite("newimage.jpg", image)
