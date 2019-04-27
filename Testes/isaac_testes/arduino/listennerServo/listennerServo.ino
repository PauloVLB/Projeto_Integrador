 #include <ros.h>
#include <std_msgs/Int8.h>
#include <Servo.h>

ros::NodeHandle nh;

Servo sDir;
Servo sEsq;

void messageCb(const std_msgs::Int8& msg) {

  int valorLido = msg.data;
  int ang = 0;

  if (valorLido <= 63) {
  	ang = map(valorLido, 0, 63, 0, 180);   
    sEsq.write(ang);
  } else {
  	ang = map(valorLido, 63, 127, 0, 180);
  	sDir.write(	ang);
  }

  /*float ang = 0;
  if (valorReal < 200.0) {
    ang = map(valorReal, 0, 200, 0, 180);   
    sEsq.write(ang);
  } else {
    ang = map(valorReal, 200, 400, 0, 180);
    sDir.write(180 - ang);
  }*/

}

ros::Subscriber<std_msgs::Int8> sub("rosserial/coordenadas", &messageCb);

void setup() {

  sDir.attach(8);
  sEsq.attach(9);

  nh.initNode();
  nh.subscribe(sub);
}

void loop(){
  nh.spinOnce();
}

