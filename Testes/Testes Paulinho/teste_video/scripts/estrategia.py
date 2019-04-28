#!/usr/bin/env python

import rospy
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

    rospy.Subscriber('relfetancia_topic', Float32MultiArray, refletanciaCb)
    rospy.Subscriber('sonares_topic', Float32MultiArray, sonaresCb)
    rospy.Subscriber('sensores_cor_topic', Float32MultiArray, sensoresCorCb)

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
