#!/usr/bin/env python3
# --- ero_noisy_odometrie_4_imu_test.py ------
# Version vom 28.5.2021 by OJ
#
# verrauschte Odometry erzeugen um IMU/EKF zu testen
# ------------------------------------------------
# starten der Simulation mit IMU
# $ roslaunch ero whs_summit_xl_4mapping_imu.launch
# $ rosrun ero ero_noisy_odometrie_4_imu_test.py
# RViz die beiden Odometry - Topics vergleichen
# /robot/robotnik_base_control/odom - unverrauscht
# /noisy_odom - verrauscht
# /robot/odometry/filtered_odom  - vom EKF
# -------------------------------------------------
# Ändern in robot_localization_odom.launch - File im Pfad
# /catkin_ws/src/summit_xl_common/summit_xl_localization/launch
# <!-- arg name="odom_topic" default="robotnik_base_control/odom"/-->
# <arg name="odom_topic" value="/noisy_odom"/>  <!-- changed by OJU for IMU Test -->


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
        random_float = random.uniform(-0.001, 0.001)
        self.noisy_odom_msg.pose.pose.position.x += random_float
        random_float = random.uniform(-0.001, 0.001)
        self.noisy_odom_msg.pose.pose.position.y += random_float
        random_float = random.uniform(-0.1, 0.1)
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


