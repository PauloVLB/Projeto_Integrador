#!/usr/bin/env python

import rospy
import message_filters
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int32MultiArray



def refletanciaCb(data):
    pubMotores = rospy.Publisher('motores', Int32MultiArray, queue_size=10)
    rate = rospy.Rate(20)
    rospy.loginfo('Refle: ' + str(data.data))
    dataMotores = Int32MultiArray()
    if(data.data[0] > 4):
        dataMotores.data = [30, 30]
    else:
        dataMotores.data = [0, 0]
    pubMotores.publish(dataMotores)
       

def sonaresCb(data):
    rospy.loginfo('Sonares: ' + str(data.data))

def sensoresCorCb(data):
    rospy.loginfo('Cor: ' + str(data.data))

def hardwareListener():
    rospy.init_node('estrategia', anonymous=True)
    '''
    subSensorCor = message_filters.Subscriber('cor', Float32MultiArray)
    subSensorCor.registerCallback(sensoresCorCb)
    '''    
    subRefle = message_filters.Subscriber('refletancia', Float64MultiArray)
    subRefle.registerCallback(refletanciaCb)
    rospy.spin()
    '''
    subSonar = message_filters.Subscriber('sonares', Float32MultiArray)
    subRefle.registerCallback(sonaresCb)
    '''
    
'''
    while not rospy.is_shutdown():
        dataMotores = Int32MultiArray()

        if(a > 4):
                dataMotores.data = [50, 50]
        else:
                dataMotores.data = [0, 0]
        pubMotores.publish(dataMotores)
       
        rate.sleep()
'''
      #rospy.spin()

if __name__ == "__main__":
	try:
		hardwareListener()
	except rospy.ROSInterruptException:
		pass
