#!/usr/bin/env python
# whs_gazebo_patrol.py
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

# Die Wegpunkte Ort (x,y,z) + Orientierung (x,y,z,w)
# Tipp: mit rostopic echo /clicked_point werden die in RVIZ
# angeklickten Punkte (Publish Point) angezeigt
waypoints = [
    [(-3.39, 1.95, 0.000), (0.000, 0.000, -0.990, 0.114)],  # per clicked point
    [(4.547, -2.71, 0.000), (0.000, 0.000, -0.775, 0.655)],
    [(-3.757, -1.03, 0.000), (0.000, 0.000, 0.010, 0.999)],
]


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
    print('Starting whs_patrol.py')
    rospy.init_node('patrol')

    # Create a simple action client
    # Liste der vorhandenen action server mit
    # rostopic list | grep -o -P '^.*(?=/feedback)'
    client = actionlib.SimpleActionClient('/robot/move_base', MoveBaseAction)
    print('Waiting for Action Server')
    client.wait_for_server()
    wayPointNr = 0

    while not rospy.is_shutdown():
        for pose in waypoints:
            next_goal_pose = set_goal_pose(pose)
            print('Robot should now go to waypoint '+str(wayPointNr)+' ')
            print(str(next_goal_pose.target_pose.pose))
            wayPointNr = wayPointNr+1
            client.send_goal(next_goal_pose)
            client.wait_for_result()

        print('######## Runde zu Ende ##########')
        wayPointNr = 0
