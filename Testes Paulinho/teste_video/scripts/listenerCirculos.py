#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def circular(img, circles):
	if (circles is not None):
		circles = np.uint16(np.around(circles))
		for i in circles[0, :]:
			center = (i[0], i[1])
			radius = i[2]

			cv2.circle(img, center, 1, (0,100,100), 3) #centro
			cv2.circle(img, center, radius, (255, 0, 255), 3) #borda
	return img

def acharCirculos(img):
	copiaImg = img.copy()

	cinza = cv2.cvtColor(copiaImg, cv2.COLOR_BGR2GRAY)
	cinza = cv2.medianBlur(cinza, 5)
	
	rows = cinza.shape[1]
    
 	circles = cv2.HoughCircles(cinza, cv2.HOUGH_GRADIENT, 0.1, rows/8, 
 		param1=100, param2=30, minRadius=20, maxRadius=100)

	copiaImg = circular(copiaImg, circles)

	return copiaImg

def callback(data):
	ponte = CvBridge()
	imgCV = ponte.imgmsg_to_cv2(data,"bgr8")

	img = acharCirculos(imgCV)

	cv2.namedWindow('LISTENER_1', cv2.WINDOW_NORMAL)
	cv2.imshow('LISTENER_1', img)
	cv2.waitKey(1)


def listenerImg():
	rospy.init_node('listenerCirculo', anonymous=False)
	rospy.Subscriber('topico_img', Image, callback)
	rospy.spin()

if __name__ == "__main__":
	listenerImg()
