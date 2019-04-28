#include <robo_hardware2.h>
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Int32MultiArray.h>

ros::NodeHandle nh;

std_msgs::Float32MultiArray dataRefletancia;
ros::Publisher pubRefletancia("refletancia_topic", &dataRefletancia);

std_msgs::Float32MultiArray dataSonares;
ros::Publisher pubSonares("sonares_topic", &dataSonares);

std_msgs::Float32MultiArray dataSensoresCor;
ros::Publisher pubSensoresCor("refletancia_topic", &dataSensoresCor);

void motoresCb(std_msgs::Int32MultiArray motores){
  robo.acionarMotores(motores.data[0], motores.data[1]);
}

ros::Subscriber<std_msgs::Int32MultiArray> sub("motores_topic", &motoresCb);


void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  nh.subscribe(sub);

  nh.advertise(pubRefletancia);
  nh.advertise(pubSonares);
  nh.advertise(pubSensoresCor);

  robo.habilitaTCS34();
}

void loop() {
  // put your main code here, to run repeatedly:
  dataRefletancia.data[0] = robo.lerSensorLinhaMaisEsq();
  dataRefletancia.data[1] = robo.lerSensorLinhaEsq();
  dataRefletancia.data[2] = robo.lerSensorLinhaDir();
  dataRefletancia.data[3] = robo.lerSensorLinhaMaisDir();

  dataSonares.data[0] = robo.lerSensorSonarFrontal();
  dataSonares.data[1] = robo.lerSensorSonarDir();
  dataSonares.data[2] = robo.lerSensorSonarEsq();

  dataSensoresCor.data[0] = robo.getHSVEsquerdo().h;
  dataSensoresCor.data[1] = robo.getHSVEsquerdo().s;
  dataSensoresCor.data[2] = robo.getHSVEsquerdo().v;

  pubRefletancia.publish(&dataRefletancia);
  pubSonares.publish(&dataSonares);
  pubSensoresCor.publish(&dataSensoresCor);

  nh.spinOnce();
}
