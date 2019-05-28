#!/usr/bin/env python

import rospy
import message_filters
import cv2
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Image
from teste_video.msg import SensoresDistanciaMsg, RefletanciaMsg, BoolStamped
from cv_bridge import CvBridge

pubMotores = rospy.Publisher('motores', Int32MultiArray, queue_size=10)
pubGarra = rospy.Publisher('garra', Int32MultiArray, queue_size=10)

def arduinoCamCb(refle, dist, circulo):

    maisEsq = refle.refletancia[0]
    esq = refle.refletancia[1]
    dir = refle.refletancia[2]
    maisDir = refle.refletancia[3]

    distFrontal =  dist.sensoresDistancia[0]
    distEsq = dist.sensoresDistancia[1]
    distDir = dist.sensoresDistancia[2]

    if circulo.existe.data:
        dataMotores.data = [25,-25]
        dataGarra.data = [90, 90]
    else:
        dataMotores.data = [0,0]
        dataGarra.data = [0, 0]

    pubGarra.publish(dataGarra)
    pubMotores.publish(dataMotores)

def arduino_cam():
    rospy.init_node('arduino_cam', anonymous=True)
    subRefle = message_filters.Subscriber('refletancia', RefletanciaMsg)
    subDistancia = message_filters.Subscriber('distancia', SensoresDistanciaMsg)
    subCam = message_filters.Subscriber('tem_circulos', BoolStamped)

    ts = message_filters.TimeSynchronizer([subRefle, subDistancia, subCam], 20)

    ts.registerCallback(arduinoCamCb)

    rospy.spin()

if __name__ == "__main__":
    try:
        ponte = CvBridge()
        dataGarra = Int32MultiArray()
        dataGarra.data = [0, 0]
        dataMotores = Int32MultiArray()
        dataMotores.data = [0, 0]
        arduino_cam()
    except rospy.ROSInterruptException:
        pass
