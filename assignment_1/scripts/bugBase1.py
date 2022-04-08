# #!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import numpy
import chapter1Question6 as ch
di_leave=np.inf

with open('../input.txt') as f:
    lines = f.readlines()
data=[]
for line in lines:
    line = line.strip()
    line = line.split(",")
    data.append(line)
# print(data)
obstacle = (data[4:])
# print(obstacle)
# P = np.array([np.array([[1, 0], [3, 0], [1, 2]]),np.array([[2, 3], [4, 1], [5, 2]])])

poly=[]
list_poly=[]
for point in obstacle:
    if point == ['']:
        list_poly.append(poly)
        poly=[]
        continue
    point=[int(x) for x in point]
    poly.append(point)
list_poly.append(poly)
P=np.array(list_poly)

def  stepInto(p,q):
    v= ch.towardsObstacle(p,q)
    inta = np.arctan2(v[1], v[0])
    x.append(x[-1] + step_size*np.cos(inta))
    y.append(y[-1] + step_size*np.sin(inta))
print("code started")

def roundCheck(q):
    if ch.dist(q,hit)<= tolerance/1.0000:
        return 1
    else: return 0
    
def leaveCheck(q,di):
    global leave
    global di_leave
    if (di<di_leave):
        di_leave=di
        leave=[x[-1],y[-1]]
    if round==1 and ch.dist(q,leave)<tolerance:
        return True
    else:
        return False


round=0
N = 0  # number of obstacles
N = len(P)
start_point = [int(lines[0][0]),int(lines[0][2])]
end_point = [int(lines[1][0]),int(lines[1][2])]
step_size = float(lines[2])
tolerance = float(lines[2])
leave=start_point.copy()
x = []
y = []
x.append(start_point[0])
y.append(start_point[1])

di = ch.dist(start_point, end_point)
theta = np.arctan((y[-1]-end_point[1])/(x[-1]-end_point[0]))
test = 1

while di > step_size: # the outer most loop for fucntioning
    dis_from_land = []
    for i in range(N): # iterating through the landmarks for getting the nearest point
        dis_from_land.append(ch.computeDistancePointToPolygon(P[i], [x[-1], y[-1]]))
        dis_land = np.asarray(dis_from_land)
    if min(dis_land[:, 0]) < tolerance:
        wait =0  # if we see a landmark nearby
        p = P[np.argmin(dis_land[:, 0])]
        hit = [x[-1],y[-1]]
        leave = [x[-1],y[-1]]
        round =0
        di_leave = di
        round = 0 # counts the number of rounds around the landmark
        # Circumnavigation starts
        for i in range(1000):
            vd = ch.computeTangentVectorToPolygon(p, [x[-1], y[-1]])[1]
            if ch.computeDistancePointToPolygon(p,[x[-1], y[-1]])[0]>0.1:
                if ch.computeTangentVectorToPolygon(p, [x[-1], y[-1]])[2]==1:
                    stepInto(p,[x[-1], y[-1]])
            # plt.scatter(x, y)
            # plt.show()
            theta = np.arctan2(vd[1], vd[0])
            x.append(x[-1] + step_size*np.cos(theta))
            y.append(y[-1] + step_size*np.sin(theta))
            di = ch.dist([x[-1], y[-1]], end_point)
            wait +=1
            if round ==0 and wait>1: round = roundCheck([x[-1], y[-1]])

            if leaveCheck([x[-1], y[-1]],di):
                plt.plot(leave[0],leave[1],marker='o',markersize=20, markeredgecolor="red")
                theta = np.arctan2(-(y[-1]-end_point[1]),-(x[-1]-end_point[0]))
                x.append(x[-1] + step_size*np.cos(theta))
                y.append(y[-1] + step_size*np.sin(theta))
                break
        theta = np.arctan2(-(y[-1]-end_point[1]),-(x[-1]-end_point[0]))
    x.append(x[-1] + step_size*np.cos(theta))
    y.append(y[-1] + step_size*np.sin(theta))
    di = ch.dist([x[-1], y[-1]], end_point)
print("point reached ", di)
plt.scatter(x, y)
plt.show()

with open("../output.txt", "w") as fo:
    for i,X in enumerate(x):
        fo.write(str(X)+","+str(y[i])+"\n")

