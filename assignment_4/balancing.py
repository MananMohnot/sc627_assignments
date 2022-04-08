#!/usr/bin/env python

import rospy
from sc627_helper.msg import ObsData
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
from tf.transformations import euler_from_quaternion
import time
import matplotlib.pyplot as plt 

print("Hello I am under water")
ANG_MAX = math.pi/18
VEL_MAX = 0.15
eps = 0.0001
r_pose, lr_pose, rr_pose = [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]
r_v, lr_v, rr_v = 0.0, 0.0, 0.0
r_w,lr_w,rr_w = 0.0, 0.0, 0.0
steps=0
t=[]
path=[]
start = time.time()

def plotData(time_list, path_list):
    wpX = [x[0] for x in path_list]
    wpY = [x[1] for x in path_list]

    plt.plot(time_list, wpX)
    plt.xlabel("Time")
    plt.ylabel("X-coordinate")
    plt.title("X vs T")
    plt.grid()
    plt.show()

    plt.plot(wpX, wpY)
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title("Robot Path")
    plt.grid()
    plt.show()

def velocity_convert(x, y, theta, vel_x, vel_y):    
    '''
    Robot pose (x, y, theta)  Note - theta in (0, 2pi)
    Velocity vector (vel_x, vel_y)
    '''

    gain_ang = 1 #modify if necessary
    
    ang = math.atan2(vel_y, vel_x)
    if ang < 0:
        ang += 2 * math.pi
    
    ang_err = min(max(ang - theta, -ANG_MAX), ANG_MAX)

    v_lin =  min(max(math.cos(ang_err) * math.sqrt(vel_x ** 2 + vel_y ** 2), -VEL_MAX), VEL_MAX)
    v_ang = gain_ang * ang_err
    return v_lin, v_ang

def callback_odom(data):
    '''
    Get robot data
    '''
    print("hello i m in odom ")
    r_pose[0]= data.pose.pose.position.x # x
    r_pose[1]=data.pose.pose.position.y # y
    r_pose[2]=euler_from_quaternion((data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w))
    r_v = data.twist.twist.linear.x # linear velocity
    r_w = data.twist.twist.angular.z # angular velocity

    #TODO add the data to a list as a function of time
    t.append(time.time()-start)
    path.append((r_pose[0], r_pose[1]))

    print(data)
    pass

def callback_left_odom(data):
    '''
    Get left robot data
    '''
    lr_pose[0]= data.pose.pose.position.x # x
    lr_pose[1]=data.pose.pose.position.y # y
    lr_pose[2]=euler_from_quaternion((data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w))
    lr_v = data.twist.twist.linear.x # linear velocity
    lr_w = data.twist.twist.angular.z # angular velocity
    print('left robot')
    print(data)
    pass

def callback_right_odom(data):
    '''
    Get right robot data
    '''
    rr_pose[0]= data.pose.pose.position.x # x
    rr_pose[1]=data.pose.pose.position.y # y
    rr_pose[2]=euler_from_quaternion((data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w))
    rr_v = data.twist.twist.linear.x # linear velocity
    rr_w = data.twist.twist.angular.z # angular velocity
    print('right robot')
    print(data)
    pass

rospy.init_node('assign4', anonymous = True)
rospy.Subscriber('/odom', Odometry, callback_odom) #topic name fixed
rospy.Subscriber('/left_odom', Odometry, callback_left_odom) #topic name fixed
rospy.Subscriber('/right_odom', Odometry, callback_right_odom) #topic name fixed

pub_vel = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
r = rospy.Rate(30)

while not rospy.is_shutdown(): #replace with balancing reached?
    k=1 # kappa or proportionality parameter
    # finding distances
    
    d_left_x = r_pose[0]-lr_pose[0]
    d_right_x = - r_pose[0] + lr_pose[0]
    d_left_y = r_pose[1]-lr_pose[1]
    d_right_y = - r_pose[1] + lr_pose[1]

    v=[0,0]
    v[0]=k*(d_right_x-d_left_x)
    v_lin, v_ang = velocity_convert(r_pose[0],r_pose[1],r_pose[2], v[0],v[1])
    # print("The velocities are", v_lin,v[0])
    #publish the velocities below
    vel_msg = Twist()
    vel_msg.linear.x = v_lin
    vel_msg.angular.z = v_ang
    pub_vel.publish(vel_msg)
    r.sleep()


    if (abs(r_v)<eps and abs(lr_v)<eps and abs(rr_v)<eps) and steps>1000:
        print("balanced")
        break

    steps+=1


    #calculate v_x, v_y as per the balancing strategy
    #Make sure your velocity vector is feasible (magnitude and direction)

    #convert velocity vector to linear and angular velocties using velocity_convert function given above


    
    #store robot path with time stamps (data available in odom topic)

plotData(t, path)





