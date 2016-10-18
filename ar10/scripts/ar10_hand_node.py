#!/usr/bin/env python
#Active8 Robots, AR10 hand ROS demonstration.
#Beta release 1.1
#Written by Nick Hornsey
#Last edited on 11/10/16

#The program below subscribes to the topic "commands" in order to recieve and execute instuctions.
#Instructions can be sent either by using the ar10_teleop_node or via the terminal directly using rostopic pub.

#For example, the following command will close the hand when executed in the ros workspace:
# rostopic pub /commands std_msgs/String 'C'

#This program is opened using the following command from the ros workspace:
# rosrun ar10 ar10_hand_node.py


from ros_ar10_class import ar10
import time
import sys
import os
import random
import serial
import subprocess

import rospy
from std_msgs.msg import String 

def listener():


    rospy.init_node('listener', anonymous=True) # defines anonymous listener node

    rospy.Subscriber('commands', String, response) # Subscribes to publisher node 'commands'
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped



def response(data): # main that is called when a message from commands is recieved
    # create hand object
    hand = ar10() 

    hand.open_hand() # opens the hand
    # entering the loop
    x=1
    while x==1:


        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data) # logs messages recieved from commands to /rosout
        option = data.data


        if option == "O":        # open the hand
            hand.open_hand()
	    x+=1
        elif option == "C":    
            hand.close_hand()
	    x+=1
        elif option == "H":   
            hand.hold_tennis_ball()
	    x+=1
        elif option == "G":    
            hand.hold_golf_ball()
	    x+=1
        elif option == "D":
            hand.demo()
	    x+=1
	elif option =="OK":
	    hand.ok()
	    x+=1
	elif option == "P":
            hand.point()
	    x+=1
        elif option == "E":
            break
        else:
            print "Invalid Option"
            time.sleep(2)
	    x+=1

    time.sleep(1)
    hand.close()

if __name__ == "__main__":
        listener()

