#!/usr/bin/env python3
# ero_publish_point_2_file.py
# ################################################################################
# edited WHS, OJ , 20.5.2021 #
# usage
#   $1 rosrun ero publish_point_2_file
#
#   click at 2D NAv Goal at RViz-Map  => save in  File
import rospy
import os
from geometry_msgs.msg import PoseStamped


def clickCB(data):
    rospy.loginfo("clicked at " + str(data.pose.position.x) +
                  " " + str(data.pose.position.y))
    cwd = os.getcwd()  # Get the current working directory (cwd)
    writeStr = cwd + "/" + "path2.txt"
    fobj = open(writeStr, 'a')
    write_str = "[(" + str(data.pose.position.x) + ", "
    write_str = write_str + str(data.pose.position.y) + ", "
    write_str = write_str + str(data.pose.position.z) + "), "
    write_str = write_str + "(" + str(data.pose.orientation.x) + ", "
    write_str = write_str + str(data.pose.orientation.y) + ", "
    write_str = write_str + str(data.pose.orientation.z) + ", "
    write_str = write_str + str(data.pose.orientation.w) + ")]\n"

    fobj.write(write_str)
    fobj.close()


if __name__ == '__main__':
    try:
        rospy.init_node('click_listner', anonymous=True)
        rospy.loginfo("Auf der RVIZ- Karte einen 2D_Nag Goal ankllicken")
        click_sub = rospy.Subscriber('/robot/move_base_simple/goal2',
                                     PoseStamped,
                                     clickCB)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            pass

    except:
        print("program close.", file=sys.stderr)
