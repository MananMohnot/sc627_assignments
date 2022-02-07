#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
import numpy
import chapter1Question6 as ch

print("code started")

N = 0  # number of obstacles
P = np.array([np.array([[1, 0], [3, 0], [1, 2]]),
             np.array([[2, 3], [4, 1], [5, 2]])])
N = len(P)
print(N)
print(P[0])
obstacle_1 = np.array([[1, 0], [3, 0], [1, 2]])
obstacle_2 = np.array([[2, 3], [4, 1], [5, 2]])
start_point = [0, 0]
end_point = [5, 3]
step_size = 0.1
tolerance = 0.1
x = []
y = []
x.append(start_point[0])
y.append(start_point[1])

di = ch.dist(start_point, end_point)
theta = np.arctan((y[-1]-end_point[1])/(x[-1]-end_point[0]))
# print(di)

while di > step_size:
    # for i in range(10):
    dis_from_land = []
    for i in range(N):
        # print(P[i])
        dis_from_land.append(
            ch.computeDistancePointToPolygon(P[i], [x[-1], y[-1]]))
        dis_land = np.asarray(dis_from_land)
    if min(dis_land[:, 0]) < tolerance:
        # print("near Obstacle")
        print(np.argmin(dis_land[:, 0]))
    # print()
    x.append(x[-1] + step_size*np.cos(theta))
    y.append(y[-1] + step_size*np.sin(theta))
    di = ch.dist([x[-1], y[-1]], end_point)
    # print(di)
print("point reached ", di)
# print(dis_land[:, 0])


# print(x)
# TODO
'''
add a circumvent function
add a leave function
'''
