#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image

def talker():

	pub = rospy.Publisher('topico_img', Image, queue_size=10)
	rospy.init_node('talkerImg', anonymous=False)
	rate = rospy.Rate(20) # 20hz
	
	cam = cv2.VideoCapture(0)

	bridge = CvBridge()

	while not rospy.is_shutdown():
		
		meta, frame = cam.read()

		frame = cv2.resize(frame, (400, 400))

		frame = cv2.flip(frame, 180)

		cv2.imshow('imagemReal', frame)

		pub.publish(bridge.cv2_to_imgmsg(frame))
		rate.sleep()

		cv2.waitKey(1)

	cam.release()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass