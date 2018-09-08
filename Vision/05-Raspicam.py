# raspistill -o output.jpg

# sudo apt-get install build-essential cmake pkg-config
# sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
# sudo apt-get install libgtk2.0-dev
# sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
# sudo apt-get install libatlas-base-dev gfortran
# wget https://bootstrap.pypa.io/get-pip.py
# sudo python get-pip.py

# pip install "picamera[array]"

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)


