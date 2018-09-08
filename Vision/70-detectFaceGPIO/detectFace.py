import cv2
import sys
import os

import RPi.GPIO as GPIO
from time import sleep

# Explicar diferenca entre GPIO.BOARD e GPIO.BCM
# The GPIO.BOARD option specifies that you are referring to the pins by the number of the pin the the plug - i.e the numbers printed on the board (e.g. P1) and in the middle of the diagrams below.
# The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number, these are the numbers after "GPIO".
# Unfortunately the BCM numbers changed between versions of the Pi1 Model B
GPIO.setmode(GPIO.BOARD)

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

GPIO.setup(03, GPIO.OUT)
pwm=GPIO.PWM(03, 50)
pwm.start(0)


def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    face_detected = False
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_detected = True
    # cv2.drawContours()

    if face_detected:
        SetAngle(90)
    else:
        SetAngle(0)

    # Display the resulting frame
    # cv2.imshow('Video', frame)  ##################################### DESCOMENTAR Quando se usa SSH -X
    cv2.imwrite(os.path.join("60-LastFrame.png"), frame)  ############# Comentar quando se usa SSH -X

    if cv2.waitKey(1) & 0xFF == ord('q'):
        pwm.stop()
        GPIO.cleanup()
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()