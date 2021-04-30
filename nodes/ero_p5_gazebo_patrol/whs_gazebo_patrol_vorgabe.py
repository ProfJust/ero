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

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Die Wegpunkte Ort (x,y,z) + Orientierung (x,y,z,w)
# Tipp: mit rostopic echo /clicked_point werden die in RVIZ
# angeklickten Punkte (Publish Point) angezeigt
waypoints = [
    [(-3.2, 0.35, 0.000), (0.000, 0.000, 0.72, 0.68)],  # per clicked point
    [(-4.0, 31.1, 0.000), (0.000, 0.000, 0.24, 0.96)],
    [(57.5, 29.6, 0.000), (0.000, 0.000, -0.47, 0.88)],
    [(62.9, -50.6, 0.000), (0.000, 0.000, -0.95, 0.32)],
    [(-64.7, -56.5, 0.000), (0.000, 0.000, 0.88, 0.48)],
    [(-50.6, 33.25, 0.000), (0.000, 0.000, 0.13, 0.99)],
]


# Helper Function to turn waypoint => MoveBaseGoal
def set_goal_pose(pose):
    goal_pose = MoveBaseGoal()  # lokales Objekt instanzieren
    # lokales Objekt mit Werten fuellen
    goal_pose.target_pose.header.frame_id = 'robot_map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    # ...   
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
            print('Robot should now go to waypoint ' + str(wayPointNr) + ' ')
            print(str(next_goal_pose.target_pose.pose))
            wayPointNr = wayPointNr+1
            client.send_goal(next_goal_pose)
            client.wait_for_result()

        print('######## Runde zu Ende ##########')
        wayPointNr = 0
