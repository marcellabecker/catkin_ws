#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt

def poseCb(data):
  global curr_pose
  curr_pose = data

if __name__ == "__main__":
  rospy.init_node("turtle_challenge")

  vel_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
  rospy.Subscriber("/turtle1/pose", Pose, poseCb)

  vel_msg = Twist()
  curr_pose = Pose()

  goal_x = float(input("X: "))
  goal_y = float(input("Y: "))

  kp_lin = 0.8
  kp_ang = 3.0

  rate = rospy.Rate(10)

  while not rospy.is_shutdown():

    delta_x = goal_x - curr_pose.x
    delta_y = goal_y - curr_pose.y
    distance = sqrt(delta_x**2 + delta_y**2)
    goal_theta = atan2(delta_y, delta_x)
    ang_distance = goal_theta - curr_pose.theta

    vel_msg.linear.x = kp_lin * distance
    vel_msg.angular.z = kp_ang * ang_distance

    vel_publisher.publish(vel_msg)

    rate.sleep()

    if abs(distance) <= 1e-1:
      rospy.loginfo("Done!!")
      break