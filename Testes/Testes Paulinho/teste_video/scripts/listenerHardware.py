#!/usr/bin/env python

import rospy
import cv2
import message_filters
from std_msgs.msg import Float32MultiArray

def callbackRefle(data):
    valorSensor = data.data[0]
    rospy.loginfo('refletancia: ' + str(valorSensor))

    if(valorSensor > 4):
        show = cv2.imread('/home/paulo/IFRN/branco.png')
    else: 
        show = cv2.imread('/home/paulo/IFRN/preto.png')
    
    show = cv2.resize(show, (500, 500))
    cv2.imshow('cor', show)
    cv2.waitKey(1)

def callbackSonar(data):
    valorSensor = data.data[0]
    rospy.loginfo('sonar: ' + str(valorSensor))

    show = cv2.imread('/home/paulo/IFRN/preto.png')
  
    raio = map(valorSensor, 1, 40, show.shape[1]/2, 1)
    centro = (show.shape[1]/2, show.shape[0]/2)
    
    show = cv2.circle(show, centro, int(raio), (0,255,0), -1)

    show = cv2.resize(show, (500, 500))
    cv2.imshow('distancia', show)
    cv2.waitKey(1)

def map(x, in_min, in_max, out_min, out_max):
    if (x > in_max): 
        x = in_max
    
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

def listenerRefletancia():
    rospy.init_node('listenerHardware', anonymous=True)
    subRefle = message_filters.Subscriber('refletancia_topic', Float32MultiArray)
    subRefle.registerCallback(callbackRefle)
    
    subSonar = message_filters.Subscriber('sonares_topic', Float32MultiArray)
    subRefle.registerCallback(callbackSonar)

    rospy.spin()

if __name__ == "__main__":
	try:
		listenerRefletancia()
	except rospy.ROSInterruptException:
		pass