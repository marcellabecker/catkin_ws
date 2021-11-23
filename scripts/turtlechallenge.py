#! /usr/bin/env python3
import rospy      #é uma biblioteca Python pura para ROS
from geometry_msgs.msg import Twist #expressa a velocidade no espaço dividida em lineares e angulares
from turtlesim.msg import Pose
from math import atan2, sqrt

def poseCb(data): #callback chamado qnd o subscriber recebe um dado do tópico
  global curr_pose
  curr_pose = data

if __name__ == "__main__":
  rospy.init_node("turtle_challenge") #inicializa o nó ROS

  vel_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10) #publicar mensagens no tópico cmd_vel
  rospy.Subscriber("/turtle1/pose", Pose, poseCb)#recebe a mensagem de coordenada da posição

  vel_msg = Twist()  
  curr_pose = Pose()

  goal_x = float(input("X: "))
  goal_y = float(input("Y: "))

  kp_lin = 0.8  #controle velocidade linear
  kp_ang = 3.0  #controle velocidade angular

  rate = rospy.Rate(10) #fazer um loop na taxa desejada que é 10 (10 vezes/s)

  while not rospy.is_shutdown():#is_shutdown () para verificar se seu programa deve sair 

    delta_x = goal_x - curr_pose.x
    delta_y = goal_y - curr_pose.y
    distance = sqrt(delta_x**2 + delta_y**2)
    goal_theta = atan2(delta_y, delta_x)
    ang_distance = goal_theta - curr_pose.theta

    vel_msg.linear.x = kp_lin * distance
    vel_msg.angular.z = kp_ang * ang_distance

    vel_publisher.publish(vel_msg) #chama o publish

    rate.sleep() #mantem a taxa desejada de loop do rate

    if abs(distance) <= 1e-1: #erro
      rospy.loginfo("Done!!") #printa DONE
      break