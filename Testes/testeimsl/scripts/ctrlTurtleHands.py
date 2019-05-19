#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8

import time

vel_msg = Twist()

def callback(data):

	vel_msg.linear.x = 2.0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0

	if (data.data > 63):
		vel_msg.angular.z = -2.0
	else:
		vel_msg.angular.z = 2.0


def talker():

	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rospy.init_node('talkerHands', anonymous=False)

	while not rospy.is_shutdown():
		sub = rospy.Subscriber('rosserial/coordenadas', Int8, callback)
		pub.publish(vel_msg)
		vel_msg.linear.x = 0
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0
		time.sleep(0.1)

if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
