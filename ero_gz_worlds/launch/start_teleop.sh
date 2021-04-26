#!/bin/bash

# -- start_teleop.sh -----
# by OJ at 29.05.2020
#
# don't forget to make it executable
#----------------------------------

# Starting ROS-Node in new Shell
#xterm -hold -e rosrun turtlesim turtle_teleop_key
gnome-terminal -e 'rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/robot/robotnik_base_control/cmd_vel'
