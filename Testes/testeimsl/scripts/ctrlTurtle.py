#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

import time

def talker():

	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	vel_msg = Twist()

	
	vel_msg.linear.x = 1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 1

	print("I'm doing what you decided what I must to do, sr!")

	tInicial = rospy.get_rostime()

	while not rospy.is_shutdown():
		
		pub.publish(vel_msg)


if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
