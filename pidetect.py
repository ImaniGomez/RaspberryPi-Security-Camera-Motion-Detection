import cv2
import numpy as np
from picamera2 import Picamera2
import time

#initialize PiCamera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format ='RGB888'
picam2.configure('preview')
picam2.start()

time.sleep(2)

#capture first frame
frame1 = picam2.capture_array()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

#mo detect loop
while True: 
	frame2 = picam2.capture_array()
	frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)
	frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

	diff = cv2.absdiff(frame1_gray, frame2_gray)
	_, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
	thresh = cv2.dilate(thresh, None, iterations=2)

	contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for contour in contours: 
		if cv2.contourArea(contour) < 1000: 
			continue
		(x, y, w, h) = cv2.boundingRect(contour)
		cv2.rectangle(frame2, (x, y), (x + w, y+ h), (0, 0, 255), 2)
	cv2.imshow('Motion Detection', frame2)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	frame1_gray = frame2_gray

cv2.destroyAllWindows
