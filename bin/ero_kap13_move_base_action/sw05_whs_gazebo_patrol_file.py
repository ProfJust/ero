#!/usr/bin/env python
# sw05_whs_gazebo_patrol_file.py
# -----------------------------------------------------------------
# Version vom 22.05.2020 mit Wegpunkten
# alle summit_xl_a werden auf robot umgestellt
#
# by OJ fuer robotik.bocholt@w-hs.de
# Ursprung: Buch von Quigley, "Prog. Robots with ROS", S161
# https://github.com/osrf/rosbook/tree/master/code/navigation/src
# Laesst den Robot nacheinander die Wegpunkte abfahren
# Notwendig: Funktionierender ROS nav stack
# ------------------------------------------------------------------

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


# Helper Function to turn waypoint => MoveBaseGoal
def set_goal_pose(pose):
    # origin = [-17.000000, 61.000000, -1.5500000]
    goal_pose = MoveBaseGoal()  # lokales Objekt instanzieren
    # lokales Objekt mit Werten fuellen
    goal_pose.target_pose.header.frame_id = 'robot_map'  # sim: summit_xl_a_map
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]
    return goal_pose


# -----------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Starting whs_patrol_file.py')
    rospy.init_node('patrol')
    
    # Goals aus Datei holen
    datei = open("points2read.txt", "r")
    text = datei.readline()  # Titelzeile to ignore
    rospy.loginfo(text)

    # Create a simple action client
    # Liste der vorhandenen action server mit
    # rostopic list | grep -o -P '^.*(?=/feedback)'
    client = actionlib.SimpleActionClient('/robot/move_base', MoveBaseAction)
    print('Waiting for Action Server')
    client.wait_for_server()
    wayPointNr = 1
  
    while not rospy.is_shutdown():
        # get next Pose 
        # read 3 lines => Point
        x_text = datei.readline()
        if x_text == '':  # EOF reached?
            rospy.loginfo("No data in file anymore : \n")
            print('######## Runde zu Ende ##########')
            break
        x = float(x_text[2:])  # ignore first letters x:
            
        y_text = datei.readline()
        y = float(y_text[2:])  # ignore first letters y:
            
        z_text = datei.readline()
        z = float(z_text[2:])  # ignore first letters z:

        # Add Orientation for Pose => should be computed later
        pose = [(x, y, z), (0.0, 0.0, 0.0, 1.0)]

        next_goal_pose = set_goal_pose(pose)
        print('Robot is on the way to waypoint '+str(wayPointNr)+' ')
        print(str(next_goal_pose.target_pose.pose) +'\n')
        wayPointNr = wayPointNr+1
        client.send_goal(next_goal_pose)
        client.wait_for_result()
        wait = raw_input("Press Enter to publish next goal...")

        

