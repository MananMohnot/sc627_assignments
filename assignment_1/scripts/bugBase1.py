<<<<<<< HEAD
#!/usr/bin/env python3
=======
# #!/usr/bin/env python3
>>>>>>> 49ebe5680ecda82ca09395b94d62d29b6c606cee

import matplotlib.pyplot as plt
import numpy as np
import numpy
import chapter1Question6 as ch
<<<<<<< HEAD
di_leave = np.inf


def stepInto(p, q):
    v = ch.towardsObstacle(p, q)
    inta = np.arctan2(v[1], v[0])
    x.append(x[-1] + step_size*np.cos(inta))
    y.append(y[-1] + step_size*np.sin(inta))


print("code started")


def roundCheck(q):
    if ch.dist(q, hit) <= tolerance/1.0000:
        return 1
    else:
        return 0


def leaveCheck(q, di):
    global leave
    global di_leave
    if (di < di_leave):
        di_leave = di
        leave = [x[-1], y[-1]]
        print("The new leave point is ", di_leave)
        print(round)
    if round == 1 and ch.dist(q, leave) < tolerance:
=======
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
>>>>>>> 49ebe5680ecda82ca09395b94d62d29b6c606cee
        return True
    else:
        return False


<<<<<<< HEAD
round = 0
N = 0  # number of obstacles
P = np.array([np.array([[1, 0], [3, 0], [1, 2]]),
             np.array([[2, 3], [4, 1], [5, 2]])])
# P = np.array([np.array([[1, 0], [3, 0], [1, 2]])])
N = len(P)
# print(N)
# print(P[0])
obstacle_1 = np.array([[1, 0], [3, 0], [1, 2]])
obstacle_2 = np.array([[2, 3], [4, 1], [5, 2]])
start_point = [0, 0]
end_point = [4, 3]
# end_point = [4, 4]
# start_point = [3, 1]
step_size = 0.1
tolerance = 0.1
leave = start_point.copy()
=======
round=0
N = 0  # number of obstacles
N = len(P)
start_point = [int(lines[0][0]),int(lines[0][2])]
end_point = [int(lines[1][0]),int(lines[1][2])]
step_size = float(lines[2])
tolerance = float(lines[2])
leave=start_point.copy()
>>>>>>> 49ebe5680ecda82ca09395b94d62d29b6c606cee
x = []
y = []
x.append(start_point[0])
y.append(start_point[1])

di = ch.dist(start_point, end_point)
theta = np.arctan((y[-1]-end_point[1])/(x[-1]-end_point[0]))
<<<<<<< HEAD
# print(di)
test = 1

while di > step_size:  # the outer most loop for fucntioning
    # for i in range(10):
    dis_from_land = []
    for i in range(N):  # iterating through the landmarks for getting the nearest point
        dis_from_land.append(
            ch.computeDistancePointToPolygon(P[i], [x[-1], y[-1]]))
        dis_land = np.asarray(dis_from_land)
    if min(dis_land[:, 0]) < tolerance:
        wait = 0  # if we see a landmark nearby
        p = P[np.argmin(dis_land[:, 0])]
        hit = [x[-1], y[-1]]
        leave = [x[-1], y[-1]]
        round = 0
        di_leave = di
        round = 0  # counts the number of rounds around the landmark
        print("The landmark is ", np.argmin(dis_land[:, 0]))
        # Circumnavigation starts
        for i in range(1000):
            vd = ch.computeTangentVectorToPolygon(p, [x[-1], y[-1]])[1]
            if ch.computeDistancePointToPolygon(p, [x[-1], y[-1]])[0] > 0.1:
                if ch.computeTangentVectorToPolygon(p, [x[-1], y[-1]])[2] == 1:
                    stepInto(p, [x[-1], y[-1]])
=======
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
>>>>>>> 49ebe5680ecda82ca09395b94d62d29b6c606cee
            # plt.scatter(x, y)
            # plt.show()
            theta = np.arctan2(vd[1], vd[0])
            x.append(x[-1] + step_size*np.cos(theta))
            y.append(y[-1] + step_size*np.sin(theta))
            di = ch.dist([x[-1], y[-1]], end_point)
<<<<<<< HEAD
            wait += 1
            if round == 0 and wait > 1:
                round = roundCheck([x[-1], y[-1]])

            if leaveCheck([x[-1], y[-1]], di):
                plt.plot(leave[0], leave[1], marker='o',
                         markersize=20, markeredgecolor="red")
                # plt.show()
                theta = np.arctan2(-(y[-1]-end_point[1]
                                     ), -(x[-1]-end_point[0]))
                x.append(x[-1] + step_size*np.cos(theta))
                y.append(y[-1] + step_size*np.sin(theta))
                print("lets leave")
                break
        print("on leave")
        theta = np.arctan2(-(y[-1]-end_point[1]), -(x[-1]-end_point[0]))

        # print(np.argmin(dis_land[:, 0]))
    print("hey leave")
    # theta = np.arctan2((y[-1]-end_point[1]),(x[-1]-end_point[0]))
    x.append(x[-1] + step_size*np.cos(theta))
    # x.append(x[-1] + step_size*np.cos(theta))
    # y.append(y[-1] + step_size*np.sin(theta))
    y.append(y[-1] + step_size*np.sin(theta))

    di = ch.dist([x[-1], y[-1]], end_point)
    # print(di)
print("point reached ", di)
# print(dis_land[:, 0])

# print(x)
print("leave is ", leave)
plt.scatter(x, y)
plt.show()
# TODO
'''
add a circumvent function
add a leave function
'''
=======
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

>>>>>>> 49ebe5680ecda82ca09395b94d62d29b6c606cee
