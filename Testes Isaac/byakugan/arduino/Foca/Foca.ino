#include <Servo.h>

Servo servoEsq, servoDir;

#define PIN_SERVO_ESQ 8
#define PIN_SERVO_DIR 7

// ros comunication
#include <robo_hardware2.h>
#include <ros.h>
#include <std_msgs/Int8.h>

#define NOME_TOPICO "rosserial/coordenadas"

ros::NodeHandle nh;

void messageCb(const std_msgs::Int8& msg) {
	
	int valorLido = msg.data;

	if (valorLido > 63) {
		int valor = map(valorLido, 63, 127, 0, 180);
		servoDir.write(valor);
	} else {
		int valor = map(valorLido, 0, 63, 0, 180);
		servoEsq.write(valor);
	} 

}

ros::Subscriber<std_msgs::Int8> sub(NOME_TOPICO, &messageCb);

void setup() {

	servoEsq.attach(PIN_SERVO_ESQ);
	servoDir.attach(PIN_SERVO_DIR);

	nh.initNode();
  	nh.subscribe(sub);

}

void loop() {

	nh.spinOnce();

}
