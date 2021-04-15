#!/usr/bin/env python
# sw03_file_write_point_click.py
#-------------------------------------------
# OJ 15.06.2020
#-------------------------------------------
# Speichert alle in RViz angeklickten Points
# (Publish Point - Button)  in ein File
#-------------------------------------------

import rospy
# rostopic info /clicked_point =>
from geometry_msgs.msg import PointStamped


def click_callback(data):
    # Callback function which is called when a new point in RViz was clicked
    rospy.loginfo("List of Published Point from RViz, End = STRG+C")
    # rostopic info /clicked_point 
    rospy.loginfo("I heard %s", data.point)
    datei = open("points2.txt", "a")
    datei.write(str(data.point))  # complete with header
    datei.write("\n")
    datei.close()


if __name__ == '__main__':
    try:
        datei = open("points2.txt", "w")
        datei.write(" List of published Points from Topic /clicked_point  \n")
        datei.close()

        rospy.init_node('click_point_to_file', anonymous=True)
        click_point_subscriber = rospy.Subscriber('/clicked_point',
                                                  PointStamped, click_callback)
        rate = rospy.Rate(10) # 10hz

        while not rospy.is_shutdown():
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
