#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher pub ("publisher", &str_msgs);

void setup() {
	nh.advertise(pub);

	str_msg = "ola marilene";
}

void loop() {
	pub.publish(&str_msgs);
	nh.spinOnce();
}