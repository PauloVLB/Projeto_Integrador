#!/usr/bin/env python

import rospy
import cv2
import message_filters
from std_msgs.msg import Float64MultiArray
from teste_video.msg import SensoresDistanciaMsg, RefletanciaMsg

def callbackRefle(refle):

    if(len(refle.refletancia) > 0):
        valorSensor = refle.refletancia
        rospy.loginfo('refletancia: ' + str(valorSensor))
        show = cv2.imread('/home/paulo/IFRN/branco.png')
        show = cv2.resize(show, (600, 150))
        w = show.shape[1]
        h = show.shape[0]
        cor = (0,0,0)

        for i in range(1, 4):
            pt1 = (i*w/4, 0)
            pt2 = (i*w/4, h)
            show = cv2.line(show, pt1, pt2, cor)

        for i in range(0, 4):
            valorSensor = refle.refletancia[i]
            if(valorSensor < 4):
                pt1 = (i*w/4, 0)
                pt2 = ((i+1)*w/4, h)
                show = cv2.rectangle(show, pt1, pt2, (0,0,0), -1)

        #show = cv2.putText(show, str(valorSensor),(w/2,h/2), cv2.FONT_HERSHEY_SIMPLEX, 1, cor)

        cv2.imshow('cor', show)
        cv2.waitKey(1)

def listenerRefletancia():
    rospy.init_node('refletanciaGUI', anonymous=True)
    subRefle = message_filters.Subscriber('refletancia', RefletanciaMsg)
    subRefle.registerCallback(callbackRefle)

    rospy.spin()

if __name__ == "__main__":
	try:
		listenerRefletancia()
	except rospy.ROSInterruptException:
		pass
