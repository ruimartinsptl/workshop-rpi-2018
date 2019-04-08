#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
__author__ = 'Rui Martins'

import os
import cv2
import time
import datetime
video_capture = cv2.VideoCapture(0)
ret, frame = video_capture.read()
timename=datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S')
frame_id = 1
# cv2.imwrite(os.path.join( "f-" + timename + "-" + '%0*d' % (5, frame_id) + ".png"), frame)
cv2.imwrite(os.path.join( "Imagem1.png"), frame)
video_capture.release()
cv2.destroyAllWindows()
