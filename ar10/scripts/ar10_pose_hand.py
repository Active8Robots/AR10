#!/usr/bin/env python
#Active8 Robots, AR10 hand posing tool
#Beta release 1.2
#Written by Nick Hornsey
#Last edited on 26/10/16

#The following program uses Parser Arguments in order to move the hand into a selection of pre-defined poses.
#This program can be run from the ROS workspace using the folowing command:

#rosrun ar10 ar10_pose_hand.py -o

#This uses argument "-o" in order to open the hand, other arguments can be found using the "-h" argument instead:

#rosrun ar10 ar10_pose_hand.py -h

from ros_ar10_class import ar10 # necessary imports in order for the program to run
import time
import sys
import os
import random
import serial
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser() #defines argument parser
    pose_group = parser.add_mutually_exclusive_group(required=True) #adds group of arguments "pose_group"
    pose_group.add_argument("-o", help = "opens the hand",action='store_true') #argument to open hand
    pose_group.add_argument("-c", help = "closes the hand",action='store_true') #argument to close hand
    pose_group.add_argument("-p", help = "points index finger",action='store_true') #argument to point finger
    pose_group.add_argument("-ok", help = "moves to ok hand position",action='store_true') # argument for ok
    pose_group.add_argument("-r", help = "moves hand to random pose",action='store_true') # argument for r
    args = parser.parse_args()
    
    if args.o: #if conditions relating to corresponding arguments
	hand = ar10()
	print ('opening hand ...')
	hand.open_hand()
	hand.wait_for_hand()
	print ('hand open')
	hand.close()

    if args.c:
	hand = ar10()
	print ('closing hand ...')
	hand.close_hand()
	hand.wait_for_hand()
	print ('hand closed')
	hand.close()

    if args.p:
	hand = ar10()
	print ('pointing finger ...')
	hand.point()
	hand.wait_for_hand()
	print ('point complete')
	hand.close()

    if args.ok:
	hand = ar10()
	print ('posing hand')
	hand.ok()
	hand.wait_for_hand()
	print ('ok complete')
	hand.close()

    if args.r:
	hand = ar10()
	print ('Randomising ...')
	hand.move(0,random.randint(4500,8000))
	hand.move(1,random.randint(4500,8000))
	hand.move(2,random.randint(4500,8000))
	hand.move(3,random.randint(4500,8000))
	hand.move(4,random.randint(4500,8000))
	hand.move(5,random.randint(4500,8000))
	hand.move(6,random.randint(4500,8000))
	hand.move(7,random.randint(4500,8000))
	hand.move(8,random.randint(4500,8000))
	hand.move(9,random.randint(4500,8000))
	hand.wait_for_hand()
	print ('Pose complete')
	hand.close()



if __name__ == "__main__":
    main()
