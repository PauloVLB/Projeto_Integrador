#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int32MultiArray

def motoresCb(vel):
    pass

def hardwareTalker():
    rospy.init_node('arudino', anonymous=True)

    pubRefletancia = rospy.Publisher('refletancia', Float64MultiArray, queue_size=10)
    pubSonares = rospy.Publisher('sonares', Float64MultiArray, queue_size=10)
    pubSensoresCor = rospy.Publisher('cor', Float64MultiArray, queue_size=10)
    rate = rospy.Rate(20)

    rospy.Subscriber('motores', Int32MultiArray, motoresCb)

    while not rospy.is_shutdown():
        dataRefletancia = Float64MultiArray()
        dataSonares = Float64MultiArray()
        dataSensoresCor = Float64MultiArray()

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
