# --- TurtleSimClassDef.py ------
# Version vom 29.4.2021 by OJ
# Definition der TurtleClass
# für den TurtleSim Node
# ------------------------------------------------
# kann in anderen Sripten importiert
#   import TurtleSimClassDef
# und dann Instanziert werden, z.B.
#   summit =
#    SummitClassDef.SummitClass("mySummit")
# ------------------------------------------------


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
# from geometry_msgs.msg import PoseWithCovarianceStamped
# Statt Pose hier die Odometrie /robot/robotnik_base_control/odom
from nav_msgs.msg import Odometry
from math import pow, atan2, sqrt


class SummitClass:  # ---- unsere Klasse fuer die Turtle-Sim ------
    # ---- Konstruktor ---
    def __init__(self, name):
        self.name = name

        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('summit_controller', anonymous=True)

        # Publisher which will publish to the topic topic_name'.
        topic_name = "/robot/pad_teleop/cmd_vel"
        self.velocity_publisher = rospy.Publisher(topic_name,
                                                  Twist, queue_size=10)
        # Instanziierung eines Twist() Objektes => siehe import
        self.vel_msg = Twist()

        # A subscriber to the topic sub_name.
        # self.update_pose is called
        # when a message of type Pose is received.
        sub_name = "/robot/robotnik_base_control/odom"
        self.pose_subscriber = rospy.Subscriber(sub_name,
                                                Odometry,
                                                self.update_pose)
        # Instanziierung eines Pose() Objektes => siehe import
        self.pose = Pose()
        self.goal = Pose()  # x, y, theta
        self.rate = rospy.Rate(10)

    def quaternion_to_euler(self, x, y, z, w):
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw = atan2(t3, t4)  # Drehung um Z-Achse in rad
        return yaw

    # ---- Empfangen der Pose ---
    def update_pose(self, data):
        # Callback function which is called when a new message
        # of type Pose is received by the subscriber.
        self.pose.x = round(data.pose.pose.position.x, 4)
        self.pose.y = round(data.pose.pose.position.y, 4)
        # rospy.loginfo(rospy.get_caller_id() + "x %s  y %s ", pose.x, pose.x)
        # orientation als Quaternion
        x = data.pose.pose.orientation.x
        y = data.pose.pose.orientation.y
        z = data.pose.pose.orientation.z
        w = data.pose.pose.orientation.w
        self.pose.theta = round(self.quaternion_to_euler(x, y, z, w), 4)

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

    def set_linear_vel(self, goal_pose, constant=0.5, lin_vel_max=0.4):
        lin_vel = constant * self.euclidean_distance(goal_pose)
        if lin_vel > lin_vel_max:
            lin_vel = lin_vel_max  # Maximum begrenzen
        self.vel_msg.linear.x = lin_vel
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0

    def set_angular_vel(self, goal_pose, constant=20.0, ang_vel_max=1.0):
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
