#!/usr/bin/env python
#Active8 Robots, AR10 Rviz control node
#Beta release 1.2
#Written by Nick Hornsey
#Last edited on 17/10/16

#The following program subscribes to the rostopic "joint_states" and then sends equivalent commands to the AR10 hand.
#The program can be run in the ros workspace using the following command:
#rosrun ar10 ar10_rviz_control_node.py

#"joint_states" are published by joint_state_publisher in Rviz.
#A URDF representation of the hand can be published using the following command from the ros workspace:
#roslaunch src/ar10_description/launch/display.launch model:=src/ar10_description/urdf/ar10.urdf

 
from ros_ar10_class import ar10
import time
import sys
import os
import random
import serial
import subprocess

import rospy
from sensor_msgs.msg import JointState

def main():

	def listener():


	    rospy.init_node('listener', anonymous=True) # defines anonymous listener node
	    rospy.Subscriber('joint_states',JointState,callback)
	    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

	def callback(msg): # callback is executed when a message is published to 'joint_states'
	    for i in range (0,27): #Look through all joints in /joint_states

	      if msg.name[i] == "servo0": #Search /joint_states for "servo0"
	        z=((((msg.position[i]-0.85)*-3500)/1.3)+8000) #Converts the joint_state into usuable motor command
		hand.move(0,int(z)) # Moves hand to match Rviz representation
		print int(z) # Prints that value to terminal

	      if msg.name[i] == "servo1":
	        z=((((msg.position[i]-0.34)*-3500)/1.16)+8000)
		hand.move(1,int(z))
		print int(z)

	      if msg.name[i] == "servo2":
	        z=((((msg.position[i]-0.17)*-3500)/1.43)+8000)
		hand.move(2,int(z))
		print int(z)

	      if msg.name[i] == "servo3":
	        z= ((((msg.position[i]-0.52)*-3500)/1.22)+8000)
		hand.move(3,int(z))
		print int(z)

	      if msg.name[i] == "servo4":
	        z=((((msg.position[i]-0.17)*-3500)/1.43)+8000)
		hand.move(4,int(z))
		print int(z)

	      if msg.name[i] == "servo5":
	        z= ((((msg.position[i]-0.52)*-3500)/1.22)+8000)
		hand.move(5,int(z))
		print int(z)

	      if msg.name[i] == "servo6":
	        z=((((msg.position[i]-0.17)*-3500)/1.43)+8000)
		hand.move(6,int(z))
		print int(z)

	      if msg.name[i] == "servo7":
	        z= ((((msg.position[i]-0.52)*-3500)/1.22)+8000)
		hand.move(7,int(z))
		print int(z)

	      if msg.name[i] == "servo8":
	        z=((((msg.position[i]-0.17)*-3500)/1.43)+8000)
		hand.move(8,int(z))
		print int(z)

	      if msg.name[i] == "servo9":
	        z= ((((msg.position[i]-0.52)*-3500)/1.22)+8000)
		hand.move(9,int(z))
		print int(z)
   	    
   	   

	
	hand = ar10() # create hand object
	listener() # start subscriber

if __name__ == "__main__":
        main()


