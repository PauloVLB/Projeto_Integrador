#!/usr/bin/env python
#identificador.py

import cv2
from cv_bridge import CvBridge

class Detect():
	def __init__ (self, imgMsg):
		self.caminho = '/opt/ros/kinetic/share/OpenCV-3.3.1-dev/'
		self.imgMsg = imgMsg

		ponte = CvBridge()
		self.imgCV = ponte.imgmsg_to_cv2(self.imgMsg, "bgr8")

	def elementos_face(self, cascade, sf=1.2, mn=5):
		copiaImg = self.imgCV.copy()
		cinza = cv2.cvtColor(copiaImg, cv2.COLOR_BGR2GRAY)

		detector = cv2.CascadeClassifier(self.caminho + cascade)
		elementos = detector.detectMultiScale(cinza, scaleFactor=sf, minNeighbors=mn)

		return elementos
