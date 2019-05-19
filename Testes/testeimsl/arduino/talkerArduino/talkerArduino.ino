#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher pub("publisherArduino", &str_msg);

char msg[13] = "hello world!";

void setup() {

	nh.initNode();
	nh.advertise(pub);

}

void loop() {
	str_msg.data = msg;
	pub.publish(&str_msg);
	nh.spinOnce();
}