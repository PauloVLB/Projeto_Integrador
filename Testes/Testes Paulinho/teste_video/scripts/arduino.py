#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray

def motoresCb(vel):
    pass

def hardwareTalker():
    rospy.init_node('arudino', anonymous=True)

    pubRefletancia = rospy.Publisher('refletancia_topic', Float32MultiArray, queue_size=10)
    pubSonares = rospy.Publisher('sonares_topic', Float32MultiArray, queue_size=10)
    pubSensoresCor = rospy.Publisher('sensores_cor_topic', Float32MultiArray, queue_size=10)
    rate = rospy.Rate(20)

    rospy.Subscriber('motores_topic', Int32MultiArray, motoresCb)

    while not rospy.is_shutdown():
        dataRefletancia = Float32MultiArray()
        dataSonares = Float32MultiArray()
        dataSensoresCor = Float32MultiArray()

        dataRefletancia.data = [random.randint(1, 15),23,23,21]
        dataSonares.data = [random.randint(1, 40),12,5]
        dataSensoresCor.data = [23, 2, 32]
        
        pubSonares.publish(dataSonares)
        pubRefletancia.publish(dataRefletancia)
        pubSensoresCor.publish(dataSensoresCor)
        
        rate.sleep()

if __name__ == "__main__":

	try:
		hardwareTalker()
	except rospy.ROSInterruptException:
		rospy.kill()
