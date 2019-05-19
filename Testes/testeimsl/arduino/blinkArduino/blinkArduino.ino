#include <ros.h>
#include <std_msgs/Int8.h>

ros::NodeHandle nh;

void callback(std_msgs::Int8& blinkNode) {

	if(blinkNode.data == 1) {
		digitalWrite(13, HIGH);
	} else {
		digitalWrite(13, LOW);
	}

}

ros::Subscriber<std_msgs::Int8> sub("blinkNode", &callback);


void setup() {

	pinMode(13, OUTPUT);
	nh.initNode();
	nh.subscribe(sub);

}

void loop() {

	nh.spinOnce();

}
