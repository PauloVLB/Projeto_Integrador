#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import message_filters
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int8MultiArray # 1byte -128 to 127, utilizamos de 0 a 90
from testevideo.msg import SensoresDistanciaMsg, RefletanciaMsg

def callbackEstrategia(refle, dist):
    pubMotores = rospy.Publisher('motores', Int32MultiArray, queue_size=10
    rate = rospy.Rate(20)

    maisEsq = refle.refletancia[0]
    esq = refle.refletancia[1]
    dir = refle.refletancia[2]
    maisDir = refle.refletancia[3]
    dataMotores = Int32MultiArray()

    if(esq > 4 and dir > 4 ) :
        dataMotores.data = [25, 25]
    elif (esq > 4 and dir < 4  ):
        dataMotores.data = [25, -25]
    elif (esq < 4 and dir > 4 ):
        dataMotores.data = [-25,25]
    elif (esq < 4 and dir < 4 ):
        dataMotores.data = [25, 25]

    pubMotores.publish(dataMotores)


def estrategia():
    rospy.init_node('estrategia', anonymous=True)
    subRefle = message_filters.Subscriber('refletancia', RefletanciaMsg)
    subDistancia = message_filters.Subscriber('distancia', SensoresDistanciaMsg)

    ts = message_filters.TimeSynchronizer([subRefle, subDistancia], 10)
    ts.registerCallback(callbackEstrategia)

    rospy.spin()

def sala3():
    pubGarra = rospy.Publisher('garra', Int8MultiArray, queue_size=10)
    rate = rospy.Rate(20)

    dataGarra = Int8MultiArray()

    dataGarra = [0,0] # braco, mão

    pubGarra.publish(dataGarra)


if __name__ == "__main__":
	try:
	      estrategia()
	except rospy.ROSInterruptException:
		pass
