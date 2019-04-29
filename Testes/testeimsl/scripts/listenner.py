#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "MSG: " + data.data);

def listenner():
	
	rospy.init_node('listenner', anonymous=False)
	rospy.Subscriber("chatter", String, callback, queue_size=10)

	rospy.spin()


if __name__ == "__main__":
	try:
		listenner()
	except rospy.ROSInterruptException:
		pass