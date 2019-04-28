#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray

def motoresCb(vel):
    pass

def hardwareTalker():
    rospy.init_node('arudino', anonymous=True)

    pubRefletancia = rospy.Publisher('relfetancia_topic', Float32MultiArray, queue_size=10)
    pubSonares = rospy.Publisher('sonares_topic', Float32MultiArray, queue_size=10)
    pubSensoresCor = rospy.Publisher('sensores_cor_topic', Float32MultiArray, queue_size=10)
    rate = rospy.Rate(20)

    rospy.Subscriber('motores_topic', Int32MultiArray, motoresCb)

    while not rospy.is_shutdown():
        dataRefletancia = Float32MultiArray()
        dataSonares = Float32MultiArray()
        dataSensoresCor = Float32MultiArray()

        dataRefletancia.data = [45,23,23,21]
        dataSonares.data = [10,12,5]
        dataSensoresCor.data = [23, 2, 32]

        pubRefletancia.publish(dataRefletancia)
        pubSonares.publish(dataSonares)
        pubSensoresCor.publish(dataSensoresCor)

        rate.sleep()

if __name__ == "__main__":

	try:
		hardwareTalker()
	except rospy.ROSInterruptException:
		pass
