# whs_patrol.py
#-----------------------------------------------------------------
# Version vom 17.01.2019 mit Wegpunkten um die Hochschule
# by OJ fuer robotik.bocholt@w-hs.de
#
# yet to be tested !!!!!!!
#
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
    [(-53.830, 29.591, 0.000), (0.000, 0.000, 0.909, -0.417)],  ### HS5 nach links
    [(-66.802, -57.131, 0.000), (0.000, 0.000, -0.393, 0.919)], ### Feuerwehrecke
    [(14.125, -54.255, 0.000), (0.000, 0.000, -0.084, 0.996)], ### BHKW
    [(63.468, -48.011, 0.000), (0.000, 0.000, 0.579, 0.816)],  #### Kueche
    [(55.520, 28.843, 0.000), (0.000, 0.000, 0.949, 0.315)],  ### HS1
]

# Helper Function to turn waypoint => MoveBaseGoal
def set_goal_pose(pose):
    #origin = [-17.000000, 61.000000, -1.5500000]
    goal_pose = MoveBaseGoal()  #lokales Objekt instanzieren
    #lokales Objekt mit Werten fuellen
    goal_pose.target_pose.header.frame_id = 'summit_xl_map' #sim: summit_xl_a_map
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
    print('Starting whs_patrol.py')
    rospy.init_node('patrol')
    
    # Create a simple action client
    # Liste der vorhandenen action server mit
    # rostopic list | grep -o -P '^.*(?=/feedback)'
    client = actionlib.SimpleActionClient('/summit_xl/move_base', MoveBaseAction)
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
            client.wait_for_result() 
            
        print('######## Runde zu Ende ##########')
        wayPointNr = 0


