#!/usr/bin/env python

import rospy
import cv2
import message_filters
from std_msgs.msg import Float64MultiArray

def callbackRefle(data):
    if(len(data.data) > 0):
        valorSensor = data.data[0]
        #rospy.loginfo('refletancia: ' + str(valorSensor))

        show = cv2.imread('/home/paulo/IFRN/branco.png')
        w = show.shape[1]
        h = show.shape[0]
        cor = (0,0,0)
        if(valorSensor < 4):
            pt1 = (w, h)
            pt2 = (0, 0)
            cor = (255,255,255)
            show = cv2.rectangle(show, pt1, pt2, (0,0,0), -1)

        show = cv2.putText(show, str(valorSensor),(w/2,h/2), cv2.FONT_HERSHEY_SIMPLEX, 1, cor) 
        show = cv2.resize(show, (500, 500))
        cv2.imshow('cor', show)
        cv2.waitKey(1)

def callbackSonar(data):
    if(len(data.data) > 0):
        valorSensor = data.data[0]
        rospy.loginfo('sonar: ' + str(valorSensor))

        show = cv2.imread('/home/paulo/IFRN/branco.png')
        w = show.shape[1]
        h = show.shape[0]

        raio = map(valorSensor, 1, 40, w/2, 1)
        centro = (w/2, h/2)
        
        show = cv2.circle(show, centro, int(raio), (0,255,0), -1)

        show = cv2.putText(show, str(valorSensor),(w/2,h/2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
        show = cv2.resize(show, (500, 500))
        cv2.imshow('distancia', show)
        cv2.waitKey(1)

def map(x, in_min, in_max, out_min, out_max):
    if (x > in_max): 
        x = in_max
    
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

def listenerRefletancia():
    rospy.init_node('listenerHardware', anonymous=True)
    subRefle = message_filters.Subscriber('refletancia', Float64MultiArray)
    subRefle.registerCallback(callbackRefle)
    
    subSonar = message_filters.Subscriber('sonares', Float64MultiArray)
    subSonar.registerCallback(callbackSonar)
    
    rospy.spin()

if __name__ == "__main__":
	try:
		listenerRefletancia()
	except rospy.ROSInterruptException:
		pass