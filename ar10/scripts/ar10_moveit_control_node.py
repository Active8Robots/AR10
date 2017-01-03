#!/usr/bin/env python
#Active8 Robots, AR10 MoveIt! control node
#Beta release 1.2
#Written by Nick Hornsey
#Last edited on 11/10/16

#The following program subscribes to the rostopic "move_group/display_planned_path" and sends an array of commands to the AR10 hand in order to plan a path.
#The program can be run in the ros workspace using the following command:
#rosrun ar10 ar10_moveit_control_node.py

#Paths are published using the moveit plugin to move the end effectors of the hand.
#A URDF representation of the hand can be published using the following command from the ros workspace:
#roslaunch src/ar10_moveit/launch/demo.launch


 
from ros_ar10_class import ar10
import time
import sys
import os
import random
import serial
import subprocess

import rospy
from moveit_msgs.msg import DisplayTrajectory


def main():


	def listener():


	    rospy.init_node('listener', anonymous=True) # defines anonymous listener node
	    rospy.Subscriber('move_group/display_planned_path',DisplayTrajectory,callback)
	    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

	def callback(msg): # callback is executed when a message is published to 'move_group/display_planned_path'
	    pos = [1,1,1,1,1,1,1,1,1,1] # creates an array of 10 to store path
	    for i in range (0,47):
	     for j in range(0,1000):
	     
              for k in range(0,2): 
	       x= msg.trajectory[i].joint_trajectory.joint_names[k] # gets the names of the 2 joints that are moving    
	       pos[k]=msg.trajectory[i].joint_trajectory.points[j].positions[k]
	       time.sleep(.03)

	       if x == "servo0":  #checks the name of the servos agaisnt variety of if statements
	         z=((((pos[k]-0.85)*-3500)/1.3)+8000) # converts the joint positions from moveit to servo commands for the AR10
	         hand.move(0,int(z))     #sends commands to the AR10

	       if x == "servo1":
	         z=((((pos[k]-0.34)*-3500)/1.16)+8000)
	         hand.move(1,int(z))


	       if x == "servo2":
	         z=((((pos[k]-0.17)*-3500)/1.43)+8000)
	         hand.move(2,int(z))


	       if x == "servo3":
	         z= ((((pos[k]-0.52)*-3500)/1.22)+8000)
	         hand.move(3,int(z))


	       if x == "servo4":
	         z=((((pos[k]-0.17)*-3500)/1.43)+8000)
	         hand.move(4,int(z))


	       if x == "servo5":
	         z= ((((pos[k]-0.52)*-3500)/1.22)+8000)
	         hand.move(5,int(z))


	       if x == "servo6":
	         z=((((pos[k]-0.17)*-3500)/1.43)+8000)
	         hand.move(6,int(z))


	       if x == "servo7":
	         z= ((((pos[k]-0.52)*-3500)/1.22)+8000)
	         hand.move(7,int(z))


	       if x == "servo8":
	         z=((((pos[k]-0.17)*-3500)/1.43)+8000)
	         hand.move(8,int(z))


	       if x == "servo9":
	         z= ((((pos[k]-0.52)*-3500)/1.22)+8000)
	         hand.move(9,int(z))


	
	hand = ar10() # create hand object
	listener() # start subscriber

if __name__ == "__main__":
        main()


