#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from teste_video.msg import Circulo, Circulos
from draw import DrawCircles, DrawLines, Write


def translate(circulo, img):
	circulo.x = ((img.shape[1]/2)-circulo.x)*-1
	circulo.y = ((img.shape[0]/2)-circulo.y)

def circular(img, circles):
	linha.horizontal(img)
	linha.vertical(img)

	if (circles is not None):
		circles = np.int0(np.around(circles))
		index = 1
		for i in circles[0, :]:
			circulo.x = i[0]
			circulo.y = i[1]
			circulo.raio = i[2]
			circulo.index = index
			index += 1

			circuloBorda.draw(img, circulo) #borda
			circuloCentro.draw(img, circulo) #centro
			texto.onCircles(img, circulo) #texto acima

			translate(circulo, img)
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
	arrayCirculos = Circulos()

	circuloBorda = DrawCircles((255,0,255), 3)
	circuloCentro = DrawCircles((0,100,100),3, True)
	linha = DrawLines()
	texto = Write(True)

	listenerImg()
