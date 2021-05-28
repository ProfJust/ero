#!/usr/bin/env python3
# --- ero_noisy_odometrie_4_imu_test.py ------
# Version vom 28.5.2021 by OJ
#
# verrauschte Odometry erzeugen um IMU/EKF zu testen
# ------------------------------------------------

# from https://answers.ros.org/question/370806/adding-noise-to-odom-topic/
# https://kapernikov.com/the-ros-robot_localization-package/


import rospy
from nav_msgs.msg import Odometry
import random


class odom_noise_class:
    def __init__(self):
        rospy.init_node('noisy_odom_node', anonymous=True)
        rospy.loginfo("IMU Test with noisy odometrie")
    
        self.odom_sub = rospy.Subscriber('/robot/robotnik_base_control/odom',
                                         Odometry, self.callback)
        self.noisy_odom_pub = rospy.Publisher('/noisy_odom',
                                              Odometry, queue_size=10)
        self.noisy_odom_msg = Odometry()
        # self.ctrl_c = False
        # rospy.on_shutdown(self.shutdownhook)
        self.rate = rospy.Rate(10)

    def shutdownhook(self):
        self.ctrl_c = True

    def callback(self, data):  # a callback for Gazebo odometry data
        self.noisy_odom_msg = data
        # rospy.loginfo("callback reached")
        self.add_noise()

    def add_noise(self):
        random_float = random.uniform(-0.5, 0.5)
        self.noisy_odom_msg.pose.pose.position.x += random_float
        random_float = random.uniform(-0.2, 0.2)
        self.noisy_odom_msg.pose.pose.orientation.z += random_float
        rospy.loginfo(" Adding %f", random_float)

    def publish_loop(self):
        while not rospy.is_shutdown():
            # rospy.loginfo("publishing")
            self.noisy_odom_pub.publish(self.noisy_odom_msg)
            self.rate.sleep()


if __name__ == '__main__':
    odc = odom_noise_class()
    odc.publish_loop()


