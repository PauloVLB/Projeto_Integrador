#include <ros.h>
#include <std_msgs/Int8.h>

ros::NodeHandle nh;

void messageCb(const std_msgs::Int8& msg) {
	
	digitalWrite(3, msg.data);
	
}

ros::Subscriber<std_msgs::Int8> sub("rosserial", &messageCb);

void setup() {
	pinMode(3, OUTPUT);
	
	nh.initNode();
	nh.subscribe(sub);
}

void loop(){
	nh.spinOnce();
}