#!/usr/bin/env python
# sw03_file_write_point_click.py
# ---------------------------
# 15.06.2020
# --------------------------
import rospy
# rostopic info /clicked_point =>
from geometry_msgs.msg import PointStamped

def click_callback(data):
    # Callback function which is called when a new poimnt in RViz was clicked
    rospy.loginfo("List of Published Point from RViz, End = STRG+C")
    # rostopic info /clicked_point 
    rospy.loginfo("I heard %s", data.point)
    datei = open("points.txt", "a")
    datei.write("[")
    datei.write(str(data.point.x))
    datei.write(",")
    datei.write(str(data.point.y))
    datei.write(",")
    datei.write(str(data.point.z))
    datei.write("] \n")
    datei.close()


if __name__ == '__main__':
    try:
        datei = open("points.txt", "w")
        datei.write(" List of published Points from Topic /clicked_point  ");
        datei.close()

        rospy.init_node('click_point_to_file', anonymous=True)
        click_point_subscriber = rospy.Subscriber('/clicked_point', PointStamped, click_callback)
        rate = rospy.Rate(10) # 10hz

        while not rospy.is_shutdown():
            rate.sleep()  
       
        

    except rospy.ROSInterruptException:
        pass
