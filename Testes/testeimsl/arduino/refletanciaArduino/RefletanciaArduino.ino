#include <robo_hardware2.h>
#include <ros.h>
#include <std_msgs/Float64MultiArray.h>
#include <std_msgs/Int32MultiArray.h>

ros::NodeHandle nh;

std_msgs::Float64MultiArray dataRefletancia;
ros::Publisher pubRefletancia("dataRefletancia", &dataRefletancia)

void setup() {

	nh.initNode();
	nh.advertise(pubRefletancia);

}

void loop() {

	nh.spinOnce();

}