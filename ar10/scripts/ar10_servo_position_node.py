#!/usr/bin/env python
#Active8 Robots, AR10 servo posisition publisher
#Beta release 1.2
#Written by Nick Hornsey
#Last edited on 6/10/16

# This node publishes the current servo positions of the AR10 to the topic 'servo_positions'.
# It can be run using the following command in the ros workspace terminal:
# rosrun ar10 ar10_servo_position_node.py


from ros_ar10_class import ar10
import time
import sys
import os
import random
import serial
import subprocess

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

def talker():
        pub = rospy.Publisher('servo_positions', Int32, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 1hz


	for joint in range (0, 10): # for all servos ...
	    x = hand.get_position(joint) # get servo position
	    rospy.loginfo('servo %d = %d ' , joint,x)
	    pub.publish(x) # publish servo position



        rate.sleep()


if __name__ == '__main__':
    hand = ar10()
    talker()
