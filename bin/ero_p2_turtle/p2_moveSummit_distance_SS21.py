#!/usr/bin/env python3
# --- p2_moveTurtle_distance_VORGABE.py ------
# Version vom 22.4.2021 by OJ
# ohne OOP und Klasse
# ----------------------------------
# Starten
# $1 roscore
# $2 rosrun turtlesim turtlesim_node
# $3 rosrun ero p2_moveTurtle_distance_VORGABE.py
# (vorher catkin_make und  ausführbar machen mit chmod +x)
# ------------------------------------------

import rospy
# from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped

from math import pow, atan2, sqrt, pi

# --- globale Variablen ---
# instanziere ein Objekt vom ROS-Typ Pose (s.o. => import)  
_pose = PoseWithCovarianceStamped()

# --------------------------------------------------------------
# Funktion zum holen der aktuellen Pose vom ROS
# wird als Callback vom ROS aufgerufen, wenn neue Pose vorhanden
# Schreibt in globale Variable _pose (wieso geht das hier?)
#
# Callback function which is called when a new message
# of type Pose is received by the subscriber.


def update_pose(data):
    # rospy.loginfo(rospy.get_caller_id()
    #  + "x %s  y %s  theta %s", data.x, data.y, data.theta)
    _pose.x = round(data.pose.pose.position.x, 4)
    #  _pose.y = round(data.y, 4)
    # _pose.theta = round(data.theta,  4)


# --------------------------------------------------------------
# Haupt Arbeitsfunktion, wird vom main() aufgerudfen
def move():
    # ----- Init -----
    # Creates a node with name 'turtlebot_controller' and make sure it is a
    # unique node (using anonymous=True).
    rospy.init_node('summit_controller', anonymous=True)

    # Publisher which will publish to the topic '/turtle1/cmd_vel'.
    velocity_publisher = rospy.Publisher('/robot/move_base/cmd_vel',
                                         Twist, queue_size=10)
    # instanziere ein Objekt vom ROS-Typ Twist (s.o. => import)
    vel_msg = Twist()  # enthaelt cmd_vel

    # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
    # when a message of type Pose is received.
    rospy.Subscriber('/robot/amcl_pose',
                     PoseWithCovarianceStamped,
                     update_pose)  # <= Callback-Fkt
    rate = rospy.Rate(10)

    # ---- Get the input from the user ----
    dist_x = eval(input("Set your x dist: "))
    dist_y = eval(input("Set your y dist: "))
    dist_to_go = sqrt(pow(dist_x, 2) + pow(dist_y, 2))
    sollTheta = atan2(dist_y, dist_x)

    # ---- Get start Position of Turtle - meanwhile received?
    start_x = _pose.x
    start_y = _pose.y
    rospy.loginfo("Start Pose is %s %s", start_x, start_y)
    # rospy.loginfo("Angle to turn %s ", sollTheta)
    # rospy.loginfo("Still to turn %s ", abs(_pose.theta - sollTheta))

    exit()

    # --- Turtle zuerst drehen ---
    toleranz = 0.015
    while (abs(_pose.theta - sollTheta) > toleranz):
        # erlaubter theta Bereich [-pi...pi]
        if _pose.theta > pi:
            _pose.theta = _pose.theta - 2 * pi
        elif _pose.theta < -pi:
            _pose.theta = _pose.theta + 2 * pi

        # Angular velocity in the z-axis.
        if _pose.theta - sollTheta > 0:
            vel_msg.angular.z = -0.3
            rospy.loginfo(" turn right ")
        else:
            vel_msg.angular.z = 0.3
            rospy.loginfo(" turn left ")

        rospy.loginfo("Pose is %s", _pose.theta)
        rospy.loginfo("Goal angle is %s", sollTheta)
        rospy.loginfo("Still to turn %s ", abs(_pose.theta - sollTheta))

        velocity_publisher.publish(vel_msg)  # Publishing our vel_msg
        rate.sleep()  # Publish at the desired rate

    # --- Stopping our robot after the movement is over
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.loginfo(" Robot stopped turning ")

    # --- Dann die Strecke fahren ---
    while sqrt(pow((start_x - _pose.x), 2) +
               pow((start_y - _pose.y), 2)) < abs(dist_to_go):
        # Linear velocity in the x-axis.
        vel_msg.linear.x = 0.3
        
        # Publishing our vel_msg
        velocity_publisher.publish(vel_msg)  # Publishing our vel_msg

        rospy.loginfo("Pose is %f %f %f ", _pose.x, _pose.y, _pose.theta)
        # rospy.loginfo("Distance to go %s", dist_to_go)
            
        # Publish at the desired rate.
        rate.sleep()

    # --- Stopping our robot after the movement is over.
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.loginfo("Reached aim - now stopping ")

    exit()  # Programm beenden
    # If we press control + C, the node will stop.
    # rospy.spin()


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
