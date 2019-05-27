#!/usr/bin/env python

import rospy
import message_filters
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Image
from teste_video.msg import SensoresDistanciaMsg, RefletanciaMsg
from cv_bridge import CvBridge

pubMotores = rospy.Publisher('motores', Int32MultiArray, queue_size=10)

def arduino_cam_cb(refle, dist, cam):
    maisEsq = refle.refletancia[0]
    esq = refle.refletancia[1]
    dir = refle.refletancia[2]
    maisDir = refle.refletancia[3]

    distFrontal =  dist.sensoresDistancia[0]
    distEsq = dist.sensoresDistancia[1]
    distDir = dist.sensoresDistancia[2]

    imgCV = pont.imgmsg_to_cv2(cam, "bgr8")

    cv2.imshow('img', imgCV)
    cv2.waitKey(0)

def arduino_cam():
    rospy.init_node('arduino_cam', anonymous=True)
    subRefle = message_filters.Subscriber('refletancia', RefletanciaMsg)
    subDistancia = message_filters.Subscriber('distancia', SensoresDistanciaMsg)
    subCam = message_filters.Subscriber('topico_img', Image, queue_size=10)

    ts = message_filters.TimeSynchronizer([subRefle, subDistancia, subCam], 10)
    ts.registerCallback(arduino_cam_cb)

    rospy.spin()

if __name__ == "__main__":
    try:
        ponte = CvBridge()
        arduino_cam()
    except rospy.ROSInterruptException:
        pass
