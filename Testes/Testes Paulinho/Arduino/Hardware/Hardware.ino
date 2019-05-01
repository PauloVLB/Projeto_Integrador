#include <robo_hardware2.h>
#include <ros.h>
#include <std_msgs/Float64MultiArray.h>
#include <std_msgs/Int32MultiArray.h>

ros::NodeHandle nh;

std_msgs::Float64MultiArray dataRefletancia;
ros::Publisher pubRefletancia("refletancia", &dataRefletancia);

std_msgs::Float64MultiArray dataSonares;
ros::Publisher pubSonares("sonares", &dataSonares);
/*
std_msgs::Float64MultiArray dataSensoresCor;
ros::Publisher pubSensoresCor("cor", &dataSensoresCor);
*/
void motoresCb(std_msgs::Int32MultiArray motores){
  robo.acionarMotores(motores.data[0], motores.data[1]);
}
ros::Subscriber<std_msgs::Int32MultiArray> sub("motores", &motoresCb);


void setup() {
  dataRefletancia.data_length = 4;
  dataRefletancia.data = (float*)malloc(sizeof(float)*4);
  
  dataSonares.data_length = 3;
  dataSonares.data =  (float*)malloc(sizeof(float)*3);
  /*
  dataSensoresCor.data_length = 3;
  dataSensoresCor.data = (float*)malloc(sizeof(float)*3);
  */
  nh.initNode();
  nh.subscribe(sub);

  nh.advertise(pubRefletancia);
  nh.advertise(pubSonares);
  //nh.advertise(pubSensoresCor);
  
  robo.configurar(false);

  //robo.habilitaTCS34();
}

long t;
void loop() {
  dataRefletancia.data[0] = robo.lerSensorLinhaMaisEsqSemRuido();
  dataRefletancia.data[1] = robo.lerSensorLinhaEsqSemRuido();
  dataRefletancia.data[2] = robo.lerSensorLinhaDirSemRuido();
  dataRefletancia.data[3] = robo.lerSensorLinhaMaisDirSemRuido();

  dataSonares.data[0] = robo.lerSensorSonarFrontal();
  dataSonares.data[1] = robo.lerSensorSonarDir();
  dataSonares.data[2] = robo.lerSensorSonarEsq();
  /*
  dataSensoresCor.data[0] = robo.getHSVEsquerdo().h;
  dataSensoresCor.data[1] = robo.getHSVEsquerdo().s;
  dataSensoresCor.data[2] = robo.getHSVEsquerdo().v;
  */
  
  pubRefletancia.publish(&dataRefletancia);
  pubSonares.publish(&dataSonares);
//  pubSensoresCor.publish(&dataSensoresCor);

  nh.spinOnce();
}
