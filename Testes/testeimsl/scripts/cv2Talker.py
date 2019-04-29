#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import cv2

def talker():

	pub = rospy.Publisher('topico_img', Image, queue_size=10)
	rospy.init_node('talkerCv2', anonymous=False)
	
	cam = cv2.VideoCapture(0)

	bridge = CvBridge()

	while not rospy.is_shutdown():
		
		meta, frame = cam.read()

		frame = cv2.resize(frame, (400, 400))

		frame = cv2.flip(frame, 180)

		cv2.imshow('imagemReal', frame)



		pub.publish(bridge.cv2_to_imgmsg(frame))

		cv2.waitKey(1)

	cam.release()
	cv2.destroyAllWindows()
	

if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass