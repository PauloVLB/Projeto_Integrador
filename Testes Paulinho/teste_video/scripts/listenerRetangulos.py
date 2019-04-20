#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


def desenhar(img, contorno):
	biggestContourArea = 0
	biggestContourIdx = -1
	for i in range(len(contorno)):
		ctArea = cv2.contourArea(contorno[i])

		if(ctArea > biggestContourArea and ctArea > 2000.0):
			biggestContourArea = ctArea;
			biggestContourIdx = i;
				
		if(ctArea > 20):
			quinas = cv2.minAreaRect(contorno[i])
			box = cv2.boxPoints(quinas) 
			box = np.int0(box)

	if (biggestContourIdx >= 0):
		rect = cv2.minAreaRect(contorno[biggestContourIdx])
		quinas = cv2.boxPoints(rect) 
		quinas = np.int0(quinas)
		cv2.drawContours(img,[quinas],0,(0,0,255),2)
	
	return img

def acharRetangulos(img):
	copiaImg = img.copy()

	cinza = cv2.cvtColor(copiaImg, cv2.COLOR_BGR2GRAY)

	rtvl, dst = cv2.threshold(cinza, 80, 255, cv2.THRESH_BINARY_INV)
	im, contorno, hrcy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	copiaImg = desenhar(copiaImg, contorno)

	return copiaImg

def callback(data):
	ponte = CvBridge()
	imgCV = ponte.imgmsg_to_cv2(data,"bgr8")

	img = acharRetangulos(imgCV)

	#cv2.namedWindow('LISTENER_1', cv2.WINDOW_NORMAL)
	cv2.imshow('LISTENER_1', img)
	cv2.waitKey(1)


def listenerImg():
	rospy.init_node('listenerRetangulo', anonymous=False)
	rospy.Subscriber('topico_img', Image, callback)
	rospy.spin()

if __name__ == "__main__":
	listenerImg()