#!/usr/bin/env python
import cv2

cam = cv2.VideoCapture(1)

while(1):

	meta, frame = cam.read()

	frame = cv2.resize(frame, (400, 400))

	cv2.imshow('webcamFoca', frame)

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cam.release()
cv2.destroyAllWindows()