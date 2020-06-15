#!/usr/bin/env python
# sw03_file_write_point_click.py
# ---------------------------------
# publisht die points aus der Datei
# => rostopic echo /next_point
# ---------------------------------
# 15.06.2020
# --------------------------
import rospy
# rostopic info /clicked_point =>
from geometry_msgs.msg import PointStamped


if __name__ == '__main__':
    try:
        datei = open("points2read.txt", "r")
        text = datei.readline()  # Titelzeile
        rospy.loginfo(text)
        pub = rospy.Publisher('/next_point', PointStamped, queue_size=10)
        rospy.init_node('next_point_talker', anonymous=True)

        msg = PointStamped()
        msg.header.frame_id = "robot_map"

        while True:    
            # read 3 lines => point-message
            ignore_text = datei.readline()
            if ignore_text == '':  # EOF reached?
                rospy.loginfo("No data in file anymore : \n")
                break
            msg.point.x = float(ignore_text[2:])  # ignore first letters x:
            ignore_text = datei.readline()
            msg.point.y = float(ignore_text[2:])  # ignore first letters y:
            ignore_text = datei.readline()
            msg.point.z = float(ignore_text[2:])  # ignore first letters z:

            rospy.loginfo("Next Point to be published : \n")
            rospy.loginfo(msg.point)
            pub.publish(msg)
            wait = raw_input("Press Enter to publish next point...")
        
        datei.close()

    except rospy.ROSInterruptException:
        pass


"""
Deklaration von PointStamped

std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/Point point
  float64 x
  float64 y
  float64 z
"""

"""
header: 
  seq: 33
  stamp: 
    secs: 2220
    nsecs: 751000000
  frame_id: "robot_map"
point: 
  x: -11.3978090286
  y: -6.15711402893
  z: 0.00495529174805header: 
  seq: 34
  stamp: 
    secs: 2221
    nsecs: 846000000
  frame_id: "robot_map"
"""