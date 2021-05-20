#!/usr/bin/env python
# whs_gazebo_patrol.py
# -----------------------------------------------------------------
# Version vom 29.04.2021 mit Wegpunkten
#
# by OJ fuer robotik.bocholt@w-hs.de
# Ursprung: Buch von Quigley, "Prog. Robots with ROS", S161
# https://github.com/osrf/rosbook/tree/master/code/navigation/src
# Laesst den Robot nacheinander die Wegpunkte abfahren
# Notwendig: Funktionierender ROS nav stack
# ------------------------------------------------------------------
import os
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Die Wegpunkte Ort (x,y,z) + Orientierung (x,y,z,w)
# Tipp: mit rostopic echo /clicked_goal werden die in RViZ
# per 2D Nav Goal Pfeil angeklickten Goals angezeigt

# global
waypoints = []


def read_path_from_file():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    openStr = cwd + "/" + "path2.txt"
    rospy.loginfo("Reading Path from %s", openStr)
    with open(openStr, 'r') as fileIn:
        for line in fileIn:
            waypoints.append(eval(line))


def set_goal_pose(pose):
    goal_pose = MoveBaseGoal()  # lokales Objekt instanzieren
    # lokales Objekt mit Werten fuellen
    goal_pose.target_pose.header.frame_id = 'robot_map'
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
    print('Starting whs_patrol.py')
    rospy.init_node('patrol')

    # Create a simple action client
    # Liste der vorhandenen action server mit
    # rostopic list | grep -o -P '^.*(?=/feedback)'
    client = actionlib.SimpleActionClient('/robot/move_base', MoveBaseAction)
    print('Waiting for Action Server')
    client.wait_for_server()
    wayPointNr = 0
    read_path_from_file()

    while not rospy.is_shutdown():
        for pose in waypoints:
            next_goal_pose = set_goal_pose(pose)
            print('Robot should now go to waypoint ' + str(wayPointNr) + ' ')
            print(str(next_goal_pose.target_pose.pose))
            wayPointNr = wayPointNr+1
            client.send_goal(next_goal_pose)
            client.wait_for_result()

        print('######## Runde zu Ende ##########')
        wayPointNr = 0
