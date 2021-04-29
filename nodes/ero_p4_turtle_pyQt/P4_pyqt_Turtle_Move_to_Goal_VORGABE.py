#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QLabel)

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt


class TurtleClass:  # ---- unsere Klasse fuer die Turtle-Sim ------
    # ---- Konstruktor ---
    def __init__(self, name):
        self.name = name

        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        node_name = "/" + self.name + "/cmd_vel"
        self.velocity_publisher = rospy.Publisher(node_name,
                                                  Twist, queue_size=10)
        # Instanziierung eines Twist() Objektes => siehe import
        self.vel_msg = Twist()

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        sub_name = "/" + self.name + "/pose"
        self.pose_subscriber = rospy.Subscriber(sub_name,
                                                Pose, self.update_pose)
        # Instanziierung eines Pose() Objektes => siehe import
        self.pose = Pose()
        self.goal = Pose()  # x, y, theta
        self.rate = rospy.Rate(10)

    # ---- Empfangen der Pose ---
    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        # jetzt Member der Klasse => direkter Zugriff auf pose
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def stop_robot(self):
        # Stopping our robot after the movement is over.
        rospy.loginfo(" ######  Goal reached, Stop Robot #######")
        self.vel_msg.linear.x = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)

    def getGoalFromUser(self):
        self.stop_robot()
        print(" set Goal for ", self.name)
        self.goal.x = eval(input("Set your x goal: "))
        self.goal.y = eval(input("Set your y goal: "))

    def start_info(self):
        # Debug Info
        rospy.loginfo("Start Pose is %f %f", self.pose.x, self.pose.y)
        rospy.loginfo("Goal is       %f %f", self.goal.x, self.goal.y)
        rospy.loginfo("Distannce to Goal is  %f ",
                      self.euclidean_distance(self.goal))
        rospy.loginfo("SteeringAngle to Goal is  %f ",
                      self.steering_angle(self.goal))
        input("Hit any Key to start")

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def goal_reached(self, distance_tolerance=0.1):
        if self.euclidean_distance(self.goal) < distance_tolerance:
            return True
        else:
            return False

    def set_linear_vel(self, goal_pose, constant=0.5, lin_vel_max=1.0):
        lin_vel = constant * self.euclidean_distance(goal_pose)
        if lin_vel > lin_vel_max:
            lin_vel = lin_vel_max  # Maximum begrenzen
        self.vel_msg.linear.x = lin_vel
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0

    def set_angular_vel(self, goal_pose, constant=8.0, ang_vel_max=10.0):
        ang_vel = constant * (self.steering_angle(goal_pose) - self.pose.theta)
        if(ang_vel > ang_vel_max):
            ang_vel = ang_vel_max
        if(ang_vel < -ang_vel_max):
            ang_vel = -ang_vel_max
        self.vel_msg.angular.z = ang_vel
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0

    def pose_speed_info(self):
        rospy.loginfo("Pose is %s %s",
                      round(self.pose.x, 4),
                      round(self.pose.y, 4))
        rospy.loginfo("Speed is x: %s  theta: %s",
                      round(self.vel_msg.linear.x, 4),
                      round(self.vel_msg.angular.z, 4))

    def move2goal(self):
        # Moves the turtle to the goal

        while not self.goal_reached():
            # Linear velocity in the x-axis.
            self.set_linear_vel(self.goal)
            # Angular velocity in the z-axis.
            self.set_angular_vel(self.goal)
            # Publishing our vel_msg
            self.velocity_publisher.publish(self.vel_msg)
            # Publish at the desired rate.
            self.rate.sleep()
            # debug Info
            self.pose_speed_info()

        self.stop_robot()  # when goal is reached


class TurtleUIClass(QWidget):
    def __init__(self):  # Konstrukor
        # Konstruktor der Elternklasse aufrufen
        super(TurtleUIClass, self).__init__()
        self.initUI()

    def initUI(self):
        # Instanziierung der Widgets
        startWert = 5
        self.lcd = QLCDNumber(self)
        self.lcd.display(startWert)
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setMaximum(11)
        self.sld.setMinimum(0)
        self.sld.setValue(startWert)
        self.pbLess = QPushButton('<')
        self.pbMore = QPushButton('>')
        self.pbGo = QPushButton(' Go Turtle ')
        self.lblStatus = QLabel('Statuszeile')

        # BOX-Layout mit Widgets füllen
        vbox = QVBoxLayout()
        # 1.Reihe
        vbox.addWidget(self.lcd)
        # 2.Reihe
        vbox.addWidget(self.sld)
        # 3.Reihe
        hbox = QHBoxLayout()
        hbox.addWidget(self.pbLess)
        hbox.addWidget(self.pbMore)

        vbox.addLayout(hbox)
        # 4.Reihe
        vbox.addWidget(self.pbGo)
        # Alle Boxen ins Window setzen
        self.setLayout(vbox)

        # Signal und Slot verbinden
        self.sld.valueChanged.connect(self.lcd.display)
        self.sld.valueChanged.connect(self.lcd.display)

        self.pbLess.clicked.connect(self.SlotKlick)
        self.pbMore.clicked.connect(self.SlotKlick)
        self.pbGo.clicked.connect(self.SlotGo)

        # Fenster Konfigurieren
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ERO - PyQt - TurtleSteering')
        self.show()

    def SlotKlick(self):
        sender = self.sender()
        self.lblStatus.setText(sender.text() + ' was pressed')
        if sender.text() == '<':
            wert = self.sld.value()
            wert = wert-1
            self.sld.setValue(wert)
        else:
            wert = self.sld.value()
            wert = wert+1
            self.sld.setValue(wert)

    def SlotGo(self):
        """ Hier geht die Turtle ab """
        turtle1.goal.x = self.sld.value()
        turtle1.goal.y = self.sld.value()
        turtle1.move2goal()


if __name__ == '__main__':
    turtle1 = TurtleClass("turtle1")
    app = QApplication(sys.argv)
    ex = TurtleUIClass()
    sys.exit(app.exec_())
