#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8
import time

vel_msg = Twist()

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rospy.init_node('talkerDrawning', anonymous=False)

''' 90 
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 2.0 (DIR -2.0)
---
'''

def testeTurtle():
	'''
	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 2.0
	'''
	turnleft()
	ahead()
	turnright()
	back()

def turnleft():
	vel_msg.angular.z = 2.0
	for i in range(0, 2):
		pub.publish(vel_msg)
		time.sleep(1)
	vel_msg.angular.z = 0.0
	for i in range(0, 2):
		pub.publish(vel_msg)
		time.sleep(1)

def turnright():
	vel_msg.angular.z = 2.0
	for i in range(0, 2):
		pub.publish(vel_msg)
		time.sleep(1)
	vel_msg.angular.z = 0.0
	for i in range(0, 2):
		pub.publish(vel_msg)
		time.sleep(1)

def ahead():	
	vel_msg.linear.x = 1.0
	for i in range(0, 2):
		pub.publish(vel_msg)
		time.sleep(1)
	vel_msg.linear.x = 0.0
	for i in range(0, 2):
		pub.publish(vel_msg)
		time.sleep(1)
def back():	
	vel_msg.linear.x = -1.0
	for i in range(0, 2):
		pub.publish(vel_msg)
		time.sleep(1)
	vel_msg.linear.x = 0.0
	for i in range(0, 2):
		pub.publish(vel_msg)
		time.sleep(1)

if __name__ == "__main__":
	testeTurtle()		
