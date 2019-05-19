#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int8

def talker():

	pub = rospy.Publisher("blinkNode", Int8, queue_size=10)
	rospy.init_node("talkerNode", anonymous=False)

	while not rospy.is_shutdown():
		binario = raw_input()

		try:
			binario = int(binario)
			pub.publish(int(binario))
		except:
			print('0 ou 1!')


if __name__ == "__main__":
	talker()