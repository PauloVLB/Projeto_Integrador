#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():

	pub = rospy.Publisher('chatter', String, queue_size=256)
	rospy.init_node('talker', anonymous=False)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		
		msg = raw_input()

		rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':

	try:

		talker()

	except rospy.ROSInterruptException:
		pass