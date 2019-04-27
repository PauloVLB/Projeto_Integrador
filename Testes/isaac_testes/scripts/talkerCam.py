#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import requests
import numpy as np 

url = "http://10.160.2.13:8080/shot.jpg"

def talker():

	pub = rospy.Publisher('topico_img', Image, queue_size=10)
	rospy.init_node('talkerCam', anonymous=False)

	bridge = CvBridge()

	while not rospy.is_shutdown():
		
		img_resp = requests.get(url)
		img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
		frame = cv2.imdecode(img_arr, -1)

		frame = cv2.resize(frame, (400, 400))

		cv2.imshow('frame', frame)

		pub.publish(bridge.cv2_to_imgmsg(frame))

		cv2.waitKey(1)

	cam.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
