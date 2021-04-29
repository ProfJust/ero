#!/usr/bin/env python3
# --- p2_moveTurtle_distance_VORGABE.py ------
# Version vom 22.4.2021 by OJ
# ohne OOP und Klasse
# ----------------------------------
# Starten
# $1 roscore
# $2 roslaunch ero summit_xl_in_empty_world.launch
# $3 rosrun ero p2_moveTurtle_distance_VORGABE.py
# (vorher catkin_make und  ausführbar machen mit chmod +x)
# ------------------------------------------

import rospy
# from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
from turtlesim.msg import Pose

from math import pow, atan2, sqrt, pi

# --- globale Variablen ---
# instanziere ein Objekt vom ROS-Typ Pose (s.o. => import)
pose = Pose()

# --------------------------------------------------------------
# Converting a quaternion into euler angles (roll, pitch, yaw)
# roll is rotation around x in radians (counterclockwise)
# pitch is rotation around y in radians (counterclockwise)
# yaw is rotation around z in radians (counterclockwise)
# https://computergraphics.stackexchange.com/questions/8195/how-to-convert-euler-angles-to-quaternions-and-get-the-same-euler-angles-back-fr


def quaternion_to_euler(x, y, z, w):
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw = atan2(t3, t4)  # Drehung um Z-Achse in rad

    return yaw

# --------------------------------------------------------------
# Funktion zum holen der aktuellen Pose vom ROSs
# wird als Callback vom ROS aufgerufen, wenn neue Pose vorhanden
# Schreibt in globale Variable _pose (wieso geht das hier?)
#
# Callback function which is called when a new message
# of type Pose is received by the subscriber.


def update_pose(data):
    # Callback function which is called when a new message
    # of type Pose is received by the subscriber.
    pose.x = round(data.pose.pose.position.x, 4)
    pose.y = round(data.pose.pose.position.y, 4)
    # rospy.loginfo(rospy.get_caller_id() + "x %s  y %s ", pose.x, pose.x)
    # orientation als Quaternion
    x = data.pose.pose.orientation.x
    y = data.pose.pose.orientation.y
    z = data.pose.pose.orientation.z
    w = data.pose.pose.orientation.w
    pose.theta = round(quaternion_to_euler(x, y, z, w), 4)

# --------------------------------------------------------------
# Haupt Arbeitsfunktion, wird vom main() aufgerudfen


def move():
    # ----- Init -----
    # Creates a node with name 'turtlebot_controller' and make sure it is a
    # unique node (using anonymous=True).
    rospy.init_node('summit_controller', anonymous=True)

    # Publisher which will publish to the topic '/turtle1/cmd_vel'.
    # Achtung, nicht das selbe Topic nehmen wie im RVIZ Teleop Panel
    # velocity_publisher =
    # rospy.Publisher('/robot/robotnik_base_control/cmd_vel',
    # das pad_teleop hat eine höhere Prioritaet im TwistMux als
    # robotnik_base_control und ueberschreibt den /cmd_vel von dort
    velocity_publisher = rospy.Publisher('/robot/pad_teleop/cmd_vel',
                                         Twist, queue_size=10)
    # instanziere ein Objekt vom ROS-Typ Twist (s.o. => import)
    vel_msg = Twist()  # enthaelt cmd_vel

    # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
    # when a message of type Pose is received.
    rospy.Subscriber('/robot/amcl_pose',
                     PoseWithCovarianceStamped,
                     update_pose)  # <= Callback-Fkt
    rate = rospy.Rate(10)

    # Get the input from the user.
    dist_x = eval(input("Set your x dist: "))
    dist_y = eval(input("Set your y dist: "))

    # Wegstrecke und Orientierung der Turtle berechnen
    dist_to_go = sqrt(pow(dist_x, 2) + pow(dist_y, 2))
    sollTheta = round(atan2(dist_y, dist_x), 4)

    # Get start pose of Turtle - meanwhile received?
    start_x = pose.x
    start_y = pose.y

    # Debug ausgabe
    rospy.loginfo("Start Pose is %s %s %s", start_x, start_y, pose.theta)
    rospy.loginfo("Theta to reach %s ", sollTheta)
    # rospy.loginfo("Still to turn %s ", abs(pose.theta - sollTheta))

    vel_msg = Twist()  # Twist Nachricht instanzieren

    # --- Erst die Turtle drehen ---
    tolerance = 0.2
    while (abs(pose.theta - sollTheta) > tolerance):
        # theta auf Bereich [-pi...pi] begrenzen
        if pose.theta > pi:
            pose.theta = pose.theta - 2 * pi
        elif pose.theta < -pi:
            pose.theta = pose.theta + 2 * pi

        # set Angular velocity in the z-axis.
        if pose.theta - sollTheta > 0:
            vel_msg.angular.z = -0.3
            rospy.loginfo("turn right")
        else:
            vel_msg.angular.z = 0.3
            rospy.loginfo("turn left")
        # Debug ausgabe
        rospy.loginfo("Pose angle is %s", pose.theta)
        rospy.loginfo("Goal angle is %s", sollTheta)
        rospy.loginfo("Still to turn %s ", abs(pose.theta - sollTheta))
        velocity_publisher.publish(vel_msg)  # Publishing our vel_msg
        rate.sleep()  # Publish at the desired rate

    # Stopping our robot after the movement is over
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

    # --- Dann die Strecke fahren ---
    while sqrt(pow((start_x - pose.x), 2)
               + pow((start_y - pose.y), 2)) < abs(dist_to_go):

        # Linear velocity in the x-axis.
        vel_msg.linear.x = 0.4
        rospy.loginfo("Pose is %s %s", pose.x, pose.y)
        rospy.loginfo("Still to Go %s ",
                      dist_to_go - sqrt(pow((start_x - pose.x), 2)
                                        + pow((start_y - pose.y), 2)))
        # Publishing our vel_msg
        velocity_publisher.publish(vel_msg)

        # Publish at the desired rate.
        rate.sleep()

    # Stopping our robot after the movement is over.
    rospy.loginfo("Reached aim - now stopping ")

    # ----- hier Code einfügen ------

    exit()
    # If we press control + C, the node will stop.
    # rospy.spin()


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
