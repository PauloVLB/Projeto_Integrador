// ros comunication
#include <robo_hardware2.h>
#include <ros.h>
#include <std_msgs/Int8.h>

#define NOME_TOPICO "rosserial/coordenadas"

ros::NodeHandle nh;

void messageCb(const std_msgs::Int8& msg) {
	int valorLido = msg.data;

	if (valorLido > 63) {
		robo.acionarMotores(-50, 50);
		delay(20);
	} else {
		robo.acionarMotores(50, -50);
		delay(20);
	} 

	robo.acionarMotores(0, 0);

}

ros::Subscriber<std_msgs::Int8> sub(NOME_TOPICO, &messageCb);

void setup() {

	robo.configurar(false);

	nh.initNode();
  	nh.subscribe(sub);

}

void loop() {

	nh.spinOnce();

}
