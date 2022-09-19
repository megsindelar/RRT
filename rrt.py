##############################################
#RRT Program
##############################################

from math import dist, hypot
from random import random
from random import randint
from re import X
from turtle import circle
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.patches as patches
from matplotlib.patches import Circle
from matplotlib import colors as mcolors
import numpy as np


class Graph:
    def __init__(self,q_init, delta, K, D):
        self.q_init = q_init
        self.delta = delta
        self.K = K
        self.D = D


def random_configuration(D):
    x = np.random.randint(D[0][0], D[0][1])
    y = np.random.randint(D[1][0], D[1][1])
    q_rand = [x,y]
    return q_rand

"""Create random circles"""
def circles():
    i = randint(0,15)
    circ_pts = []
    while i > 0:
        center_x = randint(15,85)
        center_y = randint(15,85)
        center = [center_x, center_y]
        radius = randint(0,15)
        circ_pts.append([radius, center])
        i -= 1
    return circ_pts

def print_circles(circ_pts):
    circle_pts = []
    for a in range(len(circ_pts)):
        circle_pts1 = Circle(circ_pts[a][1], circ_pts[a][0], color = 'black')
        circle_pts.append(circle_pts1)
    return circle_pts

    # cent1 = [65,65]
    # cent2 = [20,20]
    # cent3 = [70,10]


    # circ_pts1 = [5, cent1]
    # circ_pts2 = [5, cent2]
    # circ_pts = [circ_pts1, circ_pts2]#, circ_pts3]

    # circle_pts1 = Circle(cent1, 5, color = 'black')
    # circle_pts2 = Circle(cent2, 5, color = 'black')
    # circle_pts = [circle_pts1, circle_pts2]
    # print(circle_pts)

def nearest_vertex(q_rand, exclude):
    global points
    closestdist = 100
    #past = []
    for i,a in enumerate(points):
        dist = np.sqrt((q_rand[0]-a[0])**2 + (q_rand[1] - a[1])**2)
        if dist < closestdist:
            closestdist = dist
            q_near = points[i]
            close_i = i
    #     past.append([points[i]])
    # print(past)
    #print(exclude)
    # if exclude > 0:
    #     past.sort()
    #     if len(past) > 1:
    #         q_near = past[exclude]
    #         q_near = q_near[0]
    #         print("q_near more items in list")
    #         print(q_near)
    #     else:
    #         q_near = points[close_i]
    #         print("q_near 1 item in list")
    #         print(q_near)
    return q_near

         
def new_configuration(q_near, q_rand, delta, circle_points):
    global count, goal, points, reached_goal, path
    #print(q_rand)
    #print(q_near)

    #unit vector
    #print("start")
    #print(q_rand)
    #print(q_near)
    vector = np.subtract(q_rand, q_near)
    #print(vector)
    #vector = vector[0]
    #print(vector)
    vector = [vector[0], vector[1]]
    vector_mag = np.sqrt((vector[0]**2 + vector[1]**2))
    uv_x = vector[0]/vector_mag
    uv_y = vector[1]/vector_mag
    uv = [uv_x, uv_y]

    x = delta*uv_x
    y = delta*uv_y
    #print(x, y)
    x_new = q_near[0] + x
    y_new = q_near[1] + y 
    # #print(q_near)
    # if q_near[0] > 0 and q_near[1] > 0:
    #     """First quadrant"""
    #     x_new = q_near[0] + x
    #     y_new = q_near[1] + y  

    # elif q_near[0] < 0 and q_near[1] > 0:
    #     """Second quadrant"""
    #     x_new = q_near[0] - x
    #     y_new = q_near[1] + y

    # elif q_near[0] < 0 and q_near[1] < 0:
    #     """Third quadrant"""
    #     x_new = q_near[0] - x
    #     y_new = q_near[1] - y

    # else:
    #     """Fourth quadrant"""
    #     x_new = q_near[0] + x
    #     y_new = q_near[1] - y

    q_new = [x_new, y_new]

    intersection = 0
    # for a in range(len(circle_points)):
    #     for i in range(len(circle_points[a])):
    #         min_x = q_near[0]
    #         max_x = q_new[0]
    #         min_y = q_near[1]
    #         max_y = q_new[1]
    #         print(min_x, max_x, circle_points[a][i][0])
    #         print(min_y, max_y, circle_points[a][i][1])

    """check if point is in the circle"""
    for a in range(len(circle_points)):
        rnge = circ_pts[a][0]
        center = circ_pts[a][1]
        distan = np.sqrt((q_new[0] - center[0])**2 + (q_new[1] - center[1])**2)
        if distan <= rnge:
            print("q_new inside circle")
            intersection = 1
            #stop = 0
            #return stop
            #if (min_x <= circle_points[a][i][0] <= max_x) and (min_y <= circle_points[a][i][1] <= max_y):
                # """Circle point is in the area"""
            
                # m = (q_new[1]-q_near[1])/(q_new[0]-q_near[0])
                # y = m*(circle_points[a][i][0]-q_near[0]) + q_near[1]
                # print(y)
                # print(circle_points[a][i][1] - 0.5)
                # print(circle_points[a][i][1] + 0.5)
                # print(circle_points[a][i][0])
                # print(q_near[0])
                # if ((circle_points[a][i][1] - 0.5) <= y <= (circle_points[a][i][1] + 0.5)):
                #     """Line intersects with (or close enough to) an obstacle"""
                #     print(min_x, max_x, circle_points[a][i][0])
                #     print(min_y, max_y, circle_points[a][i][1])
                #     print("intersection")
                #     intersection = 1
            #q_near_new = nearest_vertex(q_rand, points, count)
            #print(q_near_new)
            #count+=1
            #q__new_new = new_configuration(q_near_new, q_rand, delta, circle_points)
        #else:
            #count = 1
                    # stop = 0
                    # return stop
    if intersection != 1:
        points.append(q_new)

        """Parent is the q_near, child is the q_new"""
        G.append([q_near,q_new])

        x_dist = abs(q_new[0] - goal[0])
        y_dist = abs(q_new[1] - goal[1])
        c = np.sqrt(x_dist**2 + y_dist**2)
        print(c)
        while 1 < c <= 5 and intersection == 0:
            q_rand = goal

            closestdist = 100
            #past = []
            for i,a in enumerate(points):
                dist = np.sqrt((q_rand[0]-a[0])**2 + (q_rand[1] - a[1])**2)
                if dist < closestdist:
                    closestdist = dist
                    q_near = points[i]
                    close_i = i
            print(f"near:{q_near}")
            vector = np.subtract(q_rand, q_near)
            vector = [vector[0], vector[1]]
            vector_mag = np.sqrt((vector[0]**2 + vector[1]**2))
            uv_x = vector[0]/vector_mag
            uv_y = vector[1]/vector_mag
            uv = [uv_x, uv_y]

            x = delta*uv_x
            y = delta*uv_y
            #print(x, y)
            x_new = q_near[0] + x
            y_new = q_near[1] + y 
            q_new = [x_new, y_new]
            
            intersection = 0

            for a in range(len(circle_points)):
                rnge = circ_pts[a][0]
                center = circ_pts[a][1]
                distan = np.sqrt((q_new[0] - center[0])**2 + (q_new[1] - center[1])**2)
                if distan <= rnge:
                    print("q_new inside circle")
                    intersection = 1

            points.append(q_new)

            """Parent is the q_near, child is the q_new"""
            G.append([q_near,q_new])

            x_dist = abs(q_new[0] - goal[0])
            y_dist = abs(q_new[1] - goal[1])
            #print(x_dist,y_dist)
            c = np.sqrt(x_dist**2 + y_dist**2)
            print(c)
            
        if c <= 1:
            q_near = q_new
            q_new = goal
            points.append(q_new)
            G.append([q_near, q_new])
            print("Reached goal!")
            path = [[q_new, q_near]]
            for a in reversed(range(len(G)-1)):
                path_ind = len(path)
                print(path[path_ind-1][1])
                print(f"G:  {G[a]}")
                print(f"G0:  {G[a][0]}")
                if path[path_ind-1][1] == G[a][1]:
                #if G[a-1][1] == G[a][0]:
                    """If the child's parent of the vertex is the same as the child of the next vertex on the path"""
                    path.append([G[a][1], G[a][0]])
                    #path.append([G[a-1][0],G[a][1]])
                    #prev = G[a+1][1]
            #path.append([prev, goal])
            print(path)
            reached_goal = 1
            return 0

        return q_new
 
    

G = []        

q_init = [50,50]
delta = 1
K = 1000
D = [[0,100],[0,100]]

diction = {1: [0,2], 2: [4,3]}
#print(diction)

global goal
goal = [80,80]

global path
path = []

# lst = []
# dista = {}
# dist = {1:2, 2:4, 3:1}
# print(dist.items())
# dista = dict(sorted(dist.items(), key=lambda item:item[1]))
# lst = sorted(dist.keys())
# print(dista)

global points
points = [q_init]
node = Graph(q_init, delta, K, D)
exclude = 0

global count
count = 1
global reached_goal
reached_goal = 0


# cent1 = [65,65]
# cent2 = [20,20]
# cent3 = [70,10]


# circ_pts1 = [5, cent1]
# circ_pts2 = [5, cent2]
# circ_pts = [circ_pts1, circ_pts2]#, circ_pts3]

# circle_pts1 = Circle(cent1, 5, color = 'black')
# circle_pts2 = Circle(cent2, 5, color = 'black')
# circle_pts = [circle_pts1, circle_pts2]
# print(circle_pts)

circ_pts = []
circle_pts = []
circ_pts = circles()
circle_pts = print_circles(circ_pts)


while node.K > 0:
    q_rand = random_configuration(node.D)
    q_near = nearest_vertex(q_rand, exclude)
    q_new = new_configuration(q_near, q_rand, node.delta, circ_pts)
    if reached_goal == 1:
        break
    node.K-=1


"""Plotting"""
fig, ax = plt.subplots()
ax.set_xlim(node.D[0][0],node.D[0][1])
ax.set_ylim(node.D[1][0],node.D[1][1])
#seg1 = [q_init, (51,50)]
#seg2 = [(43, 44), (22, 60)]
lc = LineCollection(G)
ax.add_collection(lc)
ax.plot(q_init[0], q_init[1], 'go')
ax.plot(goal[0], goal[1], "ro")


if reached_goal == 1:
    plt_path = LineCollection(path, color = 'red')
    ax.add_collection(plt_path)

for a in range(len(circle_pts)):
    ax.add_patch(circle_pts[a])
    
#     for i in range(len(circle_pts[a])):
#         #print(circle_pts[a][i])
#         x_c = circle_pts[a][i][0]
#         y_c = circle_pts[a][i][1]
#         plt.plot(x_c, y_c, 'ro')

plt.show()






#############
#need:
### goal state
### read task 2 to get algorithm

