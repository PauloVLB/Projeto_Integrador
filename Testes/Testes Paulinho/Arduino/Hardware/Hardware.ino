#include <robo_hardware2.h>
#include <ros.h>
#include <std_msgs/Int32MultiArray.h>
#include <teste_video/RefletanciaMsg.h>
#include <teste_video/SensoresDistanciaMsg.h>

ros::NodeHandle nh;


teste_video::RefletanciaMsg dataRefletancia;
ros::Publisher pubRefletancia("refletancia", &dataRefletancia);

teste_video::SensoresDistanciaMsg dataSonares;
ros::Publisher pubSonares("distancia", &dataSonares);
/*
std_msgs::Float64MultiArray dataSensoresCor;
ros::Publisher pubSensoresCor("cor", &dataSensoresCor);
*/
void motoresCb(std_msgs::Int32MultiArray motores){
  robo.acionarMotores(motores.data[0], motores.data[1]);
}
ros::Subscriber<std_msgs::Int32MultiArray> sub("motores", &motoresCb);


void setup() {
  nh.initNode();
  nh.subscribe(sub);

  nh.advertise(pubRefletancia);
  nh.advertise(pubSonares);
  //nh.advertise(pubSensoresCor);
  
  robo.configurar(false);

  //robo.habilitaTCS34();
}

void loop() {
  dataRefletancia.refletancia[0] = robo.lerSensorLinhaMaisEsqSemRuido();
  dataRefletancia.refletancia[1] = robo.lerSensorLinhaEsqSemRuido();
  dataRefletancia.refletancia[2] = robo.lerSensorLinhaDirSemRuido();
  dataRefletancia.refletancia[3] = robo.lerSensorLinhaMaisDirSemRuido();

  dataSonares.sensoresDistancia[0] = robo.lerSensorSonarFrontal();
  dataSonares.sensoresDistancia[1] = robo.lerSensorSonarDir();
  dataSonares.sensoresDistancia[2] = robo.lerSensorSonarEsq();
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
