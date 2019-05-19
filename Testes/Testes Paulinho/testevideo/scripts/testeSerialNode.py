#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8

def callback(data):

	print('1')

def listenner():

	rospy.init_node('arduinoNode', anonymous=False)
	rospy.Subscriber('rosserial/coordenadas', Int8, callback)

	rospy.spin()

if __name__ == "__main__":
	try:
		listenner()
	except rospy.ROSInterruptException:
		pass