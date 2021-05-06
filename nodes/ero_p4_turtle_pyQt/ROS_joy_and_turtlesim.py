#!/usr/bin/env python3
""" ROS_joy_and_turtlesim.py """
# https://andrewdai.co/xbox-controller-ros.html#rosjoy
# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

""" Version Westfälische Hochschule - ERO 6.5.21 by OJ
Voraussetzungen
    $ sudo apt-get install ros-noetic-joy
Testen welcher Joystick vorhanden ist. ( X=0, 1 oder 2)
    $ sudo jstest /dev/input/jsX
Starten
    $1 roscore
    $2 rosrun joy joy_node dev:=/dev/input/js0
Der joy_node publish die Zustandsinformationen des Joysticks
auf dem Topic /joy.
    $3 rostopic echo /joy
"""


def callback(data):
    twist = Twist()
    twist.linear.x = 4 * data.axes[1]
    twist.angular.z = 4 * data.axes[0]
    pub.publish(twist)


def start():  # Intializes everything
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)

    # starts the node
    rospy.init_node('Joy2Turtle')
    rospy.spin()


if __name__ == '__main__':
    start()
