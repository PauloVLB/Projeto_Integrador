#!/usr/bin/env python

import rospy
import cv2
import time
from picamera import PiRGBArray
from picamera import PiCamera
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def talkerImg():
    rospy.init_node('talkerImg', anonymous=True)
    pub = rospy.Publisher('topico_img', Image, queue_size=10)
    rate = rospy.Rate(10)

    ponte = CvBridge()
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    time.sleep(0.1)

    while not rospy.is_shutdown():
        frame = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
        imgCV = frame.array

        imgCV = cv2.flip(imgCV, 2)
        imgMsg = ponte.cv2_to_imgmsg(imgCV, "bgr8")
        pub.publish(imgMsg)

        rate.sleep()


if __name__ == "__main__":
	try:
		talkerImg()
	except rospy.ROSInterruptException:
		pass
