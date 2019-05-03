#include "ros/msg.h"
#include <std_msgs/Header.h>

class RefletanciaMsg {
  public:
    std_msgs::Header header;
    float refletancia[4];
};
