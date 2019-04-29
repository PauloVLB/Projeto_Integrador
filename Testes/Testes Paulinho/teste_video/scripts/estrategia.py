#!/usr/bin/env python

import rospy
import message_filters
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray


def refletanciaCb(data):
    rospy.loginfo('Refle: ' + str(data.data))

def sonaresCb(data):
    rospy.loginfo('Sonares: ' + str(data.data))

def sensoresCorCb(data):
    rospy.loginfo('Cor: ' + str(data.data))

def hardwareListener():
    rospy.init_node('estrategia', anonymous=True)
    
    subSensorCor = message_filters.Subscriber('sensores_cor_topic', Float32MultiArray)
    subSensorCor.registerCallback(sensoresCorCb)

    subRefle = message_filters.Subscriber('refletancia_topic', Float32MultiArray)
    subRefle.registerCallback(refletanciaCb)
    
    subSonar = message_filters.Subscriber('sonares_topic', Float32MultiArray)
    subRefle.registerCallback(sonaresCb)

    pubMotores = rospy.Publisher('motores_topic', Int32MultiArray, queue_size=10)
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        dataMotores = Int32MultiArray()
        dataMotores.data = [50, 50]
        pubMotores.publish(dataMotores)

        rate.sleep()


if __name__ == "__main__":
	try:
		hardwareListener()
	except rospy.ROSInterruptException:
		pass
