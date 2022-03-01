#!/usr/bin/env python3
import math
from chapter1Question6 import computeDistancePointToPolygon
from sc627_helper.msg import MoveXYAction, MoveXYGoal, MoveXYResult
import rospy
import numpy as np
import actionlib

# import other helper files if any
# reading files
f1 = open("../input.txt", "r")
for num in f1:
    print(num)


rospy.init_node('test', anonymous=True)

# Initialize client
client = actionlib.SimpleActionClient('move_xy', MoveXYAction)
client.wait_for_server()

# read input file


step_size = 0.1
# setting result as initial location
result = MoveXYResult()
result.pose_final.x = 0
result.pose_final.y = 0
result.pose_final.theta = 0  # in radians (0 to 2pi)

goal_x = 5
goal_y = 3
goal = [goal_x, goal_y]
obstacle_1 = np.array([[1, 2], [1, 0], [3, 0]])
obstacle_2 = np.array([[2, 3], [4, 1], [5, 2]])
# replace true with termination condition
while step_size > dist(goal, [result.pose_final.x, result.pose_final.y]):
    if step_size < min(computeDistancePointToPolygon(obstacle_1, [result.pose_final.x, result.pose_final.y]), computeDistancePointToPolygon(obstacle_2, [result.pose_final.x, result.pose_final.y])):

        # determine waypoint based on your algo
        # this is a dummy waypoint (replace the part below)
        wp = MoveXYGoal()
        wp.pose_dest.x = step_size*3/math.sqrt(35)+result.pose_final.x
        wp.pose_dest.y = step_size*5/math.sqrt(35)+result.pose_final.x
        # theta is the orientation of robot in radians (0 to 2pi)
        wp.pose_dest.theta = math.atan(3/5)

        # send waypoint to turtlebot3 via move_xy server
        client.send_goal(wp)

        client.wait_for_result()

        # getting updated robot location
        result = client.get_result()

        # write to output file (replacing the part below)
        print(result.pose_final.x, result.pose_final.y, result.pose_final.theta)
