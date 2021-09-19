#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":

  rospy.init_node("no_migue")
  
  vel_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
  vel_msg  = Twist()

  rate = rospy.Rate(10)

  vel_lin = float(input("Vel linear: "))
  vel_ang = float(input("Vel angular: "))

  vel_msg.linear.x = vel_lin
  vel_msg.angular.z = vel_ang

  while not rospy.is_shutdown():
    vel_publisher.publish(vel_msg)
    rospy.loginfo("Rodando")
    rate.sleep()