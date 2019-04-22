#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from draw import DrawFaces

def callbackCoordenadas(data):
	arrayCoordenadas.data = data.data

def callbackImg(data):
	imgCV = ponte.imgmsg_to_cv2(data, "bgr8")

	imgCV = contornoFace.draw(imgCV, arrayCoordenadas.data)

	cv2.namedWindow('FACES', cv2.WINDOW_NORMAL)
	cv2.imshow('FACES', imgCV)
	cv2.waitKey(1)


def listenerCoordenadas():
	rospy.init_node('showFaces', anonymous=True)
	rospy.Subscriber('coordenadas_detectadas', Float64MultiArray, callbackCoordenadas)
	rospy.Subscriber('topico_img', Image, callbackImg)
	rospy.spin()

if __name__ == '__main__':
	arrayCoordenadas = Float64MultiArray()
	arrayCoordenadas.data = [0,0,0,0]
	ponte = CvBridge()
	contornoFace = DrawFaces()

	listenerCoordenadas()
