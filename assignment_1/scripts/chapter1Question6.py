#! /usr/bin/env python3

import math
import re
import numpy as np
# TODO
# add a same  point condition


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def slope(p1, p2):
    if (p2[0] == p1[0]):
        return 99999
    else:
        return (p2[1]-p1[1])/(p2[0]-p1[0])


def computeLineThroughTwoPoints(p1, p2):
    m = slope(p1, p2)
    c = p1[1]-m*p1[0]
    k = math.sqrt(1 + m*m)
    # print((1+m*m)/(k*k))
    return [m/k, -1/k, c/k]


def distancePointToLine(p0, p1, p2):
    t = computeLineThroughTwoPoints(p1, p2)
    return abs(p0[0]*t[0]+p0[1]*t[1]+t[2])


def computeDistancePointToSegment(q, p1, p2):
    d1 = dist(p1, p2)
    d2 = dist(p1, q)
    d3 = dist(p2, q)
    #print(d1**2, d2**2, d3**2)
    if (d3**2) - ((d2**2) + (d1**2)) > 0.00001:
        return 1
    elif (d2**2) - ((d1**2) + (d3**2)) > 0.00001:
        return 2
    else:
        return 0


def computeDistancePointToPolygon(P, q):
    # TODO make special condition if point inside the polygon
    n = len(P)
    flag = 0
    v = 0
    perp_dist = []
    for i in range(n):
        #print(computeDistancePointToSegment(q, P[i], P[(i+1) % n]))
        if computeDistancePointToSegment(q, P[i], P[(i+1) % n]) == 0:
            #print(distancePointToLine(q, P[i], P[(i+1) % n]))
            perp_dist.append(distancePointToLine(
                q, P[i], P[(i+1) % n]))
            if flag == 0:
                min_d = perp_dist[0]
                v = [P[(i+1) % n][0]-P[i][0], P[(i+1) % n][1]-P[i][1]]
                flag = 1
            if perp_dist[-1] < min_d:
                min_d = perp_dist[-1]
                v = [P[(i+1) % n][0]-P[i][0], P[(i+1) % n][1]-P[i][1]]
    v = v/np.sqrt((v[0]**2)+(v[1]**2))
    return [min(perp_dist), (v)]


def computeTangentVectorToPolygon(P, q):
    n = len(P)
    flag = 0
    perp_dist = []
    for i in range(n):
        perp_dist.append(dist(P[i], q))
        if flag == 0:
            min_d = perp_dist[0]
            v = [q[0]-P[i][0], q[1]-P[i][1]]
            flag = 1
        if perp_dist[-1] < min_d:
            min_d = perp_dist[-1]
            v = [q[0]-P[i][0], q[1]-P[i][1]]
    v = v/np.sqrt((v[0]**2)+(v[1]**2))
    tmp = v[0]
    v[0] = -v[1]
    v[1] = tmp
    if(min_d < computeDistancePointToPolygon(P, q)[0]):
        return [min_d, v]
    else:
        return [min_d, computeDistancePointToPolygon(P, q)[1]]

    # for i in range(n):
if __name__ == '__main__':
    p1 = [1, 0]
    p2 = [1, 1]
    q = [0, 2]

    P = np.array([[0, 0], [1, 0], [0, 1]])
    #t = computeLineThroughTwoPoints(p1, p2)
    #d = distancePointToLine(q, p1, p2)
    #k = computeDistancePointToSegment(q, p1, p2)
    l = computeTangentVectorToPolygon(P, q)
    print(l)
