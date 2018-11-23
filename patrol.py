#patrol.py
#-----------------------------------------------------------------
# Version vom 23.11.2018 
# by OJ fuer robotik.bocholt@w-hs.de
# Ursprung: Buch von Quigley, "Prog. Robots with ROS", S161
# https://github.com/osrf/rosbook/tree/master/code/navigation/src
# Laesst den Robot nacheinander die Wegpunkte abfahren
# Notwendig: Funktionierender ROS nav stack
#------------------------------------------------------------------
#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal

# Die Wegpunkte Ort (x,y,z) + Orientierung (x,y,z,w)
# Tipp: mit rostopic echo /clicked_point werden die in RVIZ 
# angeklickten Punkte (Publish Point) angezeigt 
waypoints = [ 
    [( 11.8, -5.8, 0.0), (0.0, 0.0, 0.0, 1.0)], 
    [( 20.9, -1.4, 0.0), (0.0, 0.0, 0.0, 1.0)], 
    [( 27.9,  8.3, 0.0), (0.0, 0.0, 0.7, 0.7)],
    [( 8.2,   9.9, 0.0), (0.0, 0.0, 1.0, 0.0)],
    [(-7.2,  10.3, 0.0), (0.0, 0.0,-0.7, 0.7)],
    [(-7.2,  -1.0, 0.0), (0.0, 0.0,-0.7, 0.7)],
    [( 0.0,   0.0, 0.0), (0.0, 0.0, 0.1, 1.0)],
]

# Helper Function to turn waypoint => MoveBaseGoal
def set_goal_pose(pose):
    goal_pose = MoveBaseGoal()  #lokales Objekt instanzieren
    #lokales Objekt mit Werten fuellen
    goal_pose.target_pose.header.frame_id = 'summit_xl_a_map' #alt: map
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]
    return goal_pose
    
#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    print('Starting patrol.py')
    rospy.init_node('patrol')
    
    # Create a simple action client
    # Liste der vorhandenen action server mit
    # rostopic list | grep -o -P '^.*(?=/feedback)'
    client = actionlib.SimpleActionClient('summit_xl_a/move_base', MoveBaseAction)
    print('Waiting for Action Server')
    client.wait_for_server()
    wayPointNr = 0
    
    while not rospy.is_shutdown():
        for pose in waypoints:
            next_goal_pose = set_goal_pose(pose)  
            print('Robot should now go to waypoint '+str(wayPointNr)+' ')
            print(str(next_goal_pose.target_pose.pose))
            wayPointNr = wayPointNr+1
            client.send_goal(next_goal_pose)
            #print(str(client.get_Feedback())) geht nicht
            client.wait_for_result() 
            
        print('Runde zu Ende ')
        wayPointNr = 0

##So geht's mit dem Action Server in der shell
##
##rostopic pub --once /summit_xl_a/move_base/goal move_base_msgs/MoveBaseActionGoal '{header: {frame_id: 'summit_xl_a_map'}, goal: {target_pose: {header: {frame_id: 'summit_xl_a_map'}, pose: {position: {x: 7.9, y: -5.4, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.01, w: 1.0}}}}}'
##
## gelegntlich local costmap aufraeumen mit
## rosservice call /summit_xl_a/move_base/clear_costmaps
##
## home/oj/catkin_ws/src/summit_xl_common/summit_xl_localization/maps/willow_garage.pgm
## ggf besser malen
