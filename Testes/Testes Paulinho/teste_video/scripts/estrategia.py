#!/usr/bin/env python

import rospy
import message_filters
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int32MultiArray
from teste_video.msg import SensoresDistanciaMsg, RefletanciaMsg



def callbackEstrategia(refle, dist):
    pubMotores = rospy.Publisher('motores', Int32MultiArray, queue_size=10)
    rate = rospy.Rate(20)
    dataMotores = Int32MultiArray()
    if(refle.refletancia[0] > 4):
        dataMotores.data = [30, 30]
    else:
        dataMotores.data = [0, 0]
    pubMotores.publish(dataMotores)


def estrategia():
    rospy.init_node('estrategia', anonymous=True)
    subRefle = message_filters.Subscriber('refletancia', RefletanciaMsg)
    subDistancia = message_filters.Subscriber('distancia', SensoresDistanciaMsg)

    ts = message_filters.TimeSynchronizer([subRefle, subDistancia], 10)
    ts.registerCallback(callbackEstrategia)

    rospy.spin()

if __name__ == "__main__":
	try:
	      estrategia()
	except rospy.ROSInterruptException:
		pass
