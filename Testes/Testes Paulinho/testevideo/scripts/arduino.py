#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int32MultiArray
from teste_video.msg import SensoresDistanciaMsg, RefletanciaMsg

def motoresCb(vel):
    pass

def hardwareTalker():
    rospy.init_node('arudino', anonymous=True)

    pubRefletancia = rospy.Publisher('refletancia', RefletanciaMsg, queue_size=10)
    pubSonares = rospy.Publisher('distancia', SensoresDistanciaMsg, queue_size=10)
    #pubSensoresCor = rospy.Publisher('cor', Float64MultiArray, queue_size=10)
    rate = rospy.Rate(20)

    rospy.Subscriber('motores', Int32MultiArray, motoresCb)

    while not rospy.is_shutdown():
        dataRefletancia = RefletanciaMsg()
        dataSonares = SensoresDistanciaMsg()
        #dataSensoresCor = Float64MultiArray()

        dataRefletancia.refletancia = [random.randint(1, 15),23,23,21]
        dataSonares.sensoresDistancia = [random.randint(1, 40),12,5]
        #dataSensoresCor.data = [23, 2, 32]

        pubSonares.publish(dataSonares)
        pubRefletancia.publish(dataRefletancia)
        #pubSensoresCor.publish(dataSensoresCor)

        rate.sleep()

if __name__ == "__main__":

	try:
		hardwareTalker()
	except rospy.ROSInterruptException:
		rospy.kill()
