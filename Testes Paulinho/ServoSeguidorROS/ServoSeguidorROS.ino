#include <ros.h>
#include <std_msgs/Float64MultiArray.h>
#include <Servo.h>

ros::NodeHandle  nh;

Servo servoY;

void callback( const std_msgs::Float64MultiArray& arrayCoordenadas){
  float x = arrayCoordenadas.data[0];
  float y = arrayCoordenadas.data[1];
  float w = arrayCoordenadas.data[2];
  float h = arrayCoordenadas.data[3];

  float face = (x+(w/2)); 
  
  servoY.write(map(face, 0, 640, 0, 180));
    
}

ros::Subscriber<std_msgs::Float64MultiArray> sub("coordenadas_detectadas", &callback );

void setup()
{ 
  servoY.attach(8);
  
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(100);
}

