#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Float64MultiArray
from teste_video.msg import Circulo, Circulos

def circular(img, circles):
	largura = img.shape[1]
	altura = img.shape[0]

	pt1 = (largura/2, altura)
	pt2 = (largura/2, 0)
	cv2.line(img, pt1, pt2, (0,255,0), 1)

	pt1 = (largura, altura/2)
	pt2 = (0, altura/2)
	cv2.line(img, pt1, pt2, (0,255,0), 1)		


	if (circles is not None):
		circles = np.uint16(np.around(circles))
		index = 1
		for i in circles[0, :]: 
			x, y, raio = i[0], i[1], i[2]

			center = (x, y)

			cv2.circle(img, center, 1, (0,100,100), 3) #centro
			cv2.circle(img, center, raio, (255, 0, 255), 3) #borda

			org = (x - raio, y - raio)

			x = ((largura/2)-x)*-1
			y = ((altura/2)-y)

			text = '%s: (%s,%s)'%(str(index), x, y)
			cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
			
			circulo.x = x
			circulo.y = y
			circulo.raio = raio
			circulo.index = index
			index += 1	
			pub.publish(circulo)
	return img

def acharCirculos(img):
	copiaImg = img.copy()

	cinza = cv2.cvtColor(copiaImg, cv2.COLOR_BGR2GRAY)
	cinza = cv2.medianBlur(cinza, 5)
	
	rows = cinza.shape[1]
    
 	circles = cv2.HoughCircles(cinza, cv2.HOUGH_GRADIENT, 0.00001, rows/8, 
 		param1=100, param2=30, minRadius=10, maxRadius=100)

	copiaImg = circular(copiaImg, circles)

	return copiaImg

def callback(data):
	ponte = CvBridge()
	imgCV = ponte.imgmsg_to_cv2(data,"bgr8")

	img = acharCirculos(imgCV)

	#cv2.namedWindow('LISTENER_1', cv2.WINDOW_NORMAL)
	cv2.imshow('LISTENER_1', img)
	cv2.waitKey(1)

def listenerImg():
	rospy.init_node('listenerCirculo', anonymous=False)
	rospy.Subscriber('topico_img', Image, callback)
	rospy.spin()

if __name__ == "__main__":
	pub = rospy.Publisher('coordenadas_circulos', Circulo, queue_size=10)

	circulo = Circulo()
	
	listenerImg()
