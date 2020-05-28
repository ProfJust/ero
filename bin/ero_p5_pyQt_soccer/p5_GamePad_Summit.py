#!/usr/bin/env python
""" ROS_joy_and_turtlesim.py """
# https://andrewdai.co/xbox-controller-ros.html#rosjoy

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

""" Don't forget to start Joy-Node """
""" rosrun joy joy_node dev:=/dev/input/js0 """


def callback(data):
    twist = Twist()
    # Fill Twist with data from Joy-Node
    twist.linear.x = 4*data.axes[1]
    twist.angular.z = 4*data.axes[0]
    pub.publish(twist)


def start():  # Intializes everything
    print("Joy to Summit Converter Node ist started - Don't forget to start Joy-Node")
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('/robot/pad_teleop/cmd_vel', Twist, queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2Summit')
    rospy.spin()


if __name__ == '__main__':
    start()
