Active8 Robots AR10 ROS package
README
Beta release 1.1
Last updated 17/10/16

Thank you for downloading the Active8 Robots AR10 ROS Package.

This package provides ROS compatibility to the Active Robots AR10 hand.
The package consists of the following key documents:


    ar10
      |
      |____scripts
      |       |____ar10_hand_node.py
      |       |____ar10_rviz_control_node.py
      |       |____old_ar10_rviz_control_node.py
      |       |____ar10_servo_position_node.py
      |       |____ar10_teleop_node.py
      |       |____ar10_moveit_control_node.py
      |       |____ros_ar10_class.py
      |       |____ros_AR10_calibrate.py
      |       |____ros_AR10_check_calibration.py
      |       |____ros_calibration_file
      |       |
      |   CMakeLists.txt
      |       |
      |   package.xml
      | 
ar10_description
      |
      |____launch
      |       |____display.launch
      |       |____xacrodisplay.launch
      |
      |____urdf
      |       |____ar10.urdf
      |       |____ar10simple.urdf
      |       |____ar10.urdf.xacro
      |
      |____CMakeLists.txt
      |
      |____package.xml
      |
  ar10_moveit
      |
      |____config
      |       |____ar10.srdf
      |       |____fake_controllers.yaml
      |       |____joint_limits.yaml
      |       |____kinematics.yaml
      |       |____ompl_planning.yaml
      |
      |____launch
      |       |____demo.launch
      |
      |____CMakeLists.txt
      |
      |____package.xml


INSTALLATION INSTRUCTIONS

Place the folders ar10, ar10_description, and ar10_moveit into the src folder of your ROS workspace.
For more information on how to use ROS visit http://wiki.ros.org/ROS/Tutorials
Please read the text within the scripts for further information.

Changelog
. Added new script "ar10_moveit_control_node.py" This allows users to use Moveit's collision aware path planning to control the hand.
. Updated ar10.urdf to represent the AR10 more accuratley using meshes. The old URDF has been renamed to ar10simple.urdf.
. Updated ar10_rviz_control_node.py to work with the new ar10.urdf model 
. Added "Point Finger" command to ar10_hand_node.py
. Updated the ros_AR10_calibrate.py 
