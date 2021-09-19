#! /usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def callback(msg):
  print(msg.theta)


if __name__ == "__main__":
  rospy.init_node("sub")
  
  rospy.Subscriber("/turtle1/pose", Pose, callback)
  rospy.spin()