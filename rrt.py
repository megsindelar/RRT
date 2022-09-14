##############################################
#RRT Program
##############################################

from math import dist, hypot
from re import X
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
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

def nearest_vertex(q_rand, points):
    closestdist = 100
    for i,a in enumerate(points):
        dist = np.sqrt((q_rand[0]-a[0])**2 + (q_rand[1] - a[1])**2)
        if dist < closestdist:
            closestdist = dist
            q_near = points[i]
    return q_near

         
def new_configuration(q_near, q_rand, delta, circle_points):
    #print(q_rand)
    #print(q_near)

    #unit vector
    vector = np.subtract(q_rand, q_near)
    vector_mag = np.sqrt((vector[0]**2 + vector[1]**2))
    uv_x = vector[0]/vector_mag
    uv_y = vector[1]/vector_mag
    uv = [uv_x, uv_y]

    x = delta*uv_x
    y = delta*uv_y

    if q_near[0] > 0 and q_near[1] > 0:
        """First quadrant"""
        x_new = q_near[0] + x
        y_new = q_near[1] + y  

    elif q_near[0] < 0 and q_near[1] > 0:
        """Second quadrant"""
        x_new = q_near[0] - x
        y_new = q_near[1] + y

    elif q_near[0] < 0 and q_near[1] < 0:
        """Third quadrant"""
        x_new = q_near[0] - x
        y_new = q_near[1] - y

    else:
        """Fourth quadrant"""
        x_new = q_near[0] + x
        y_new = q_near[1] - y

    q_new = [x_new, y_new]

    points.append(q_new)

    """Parent is the q_near, child is the q_new"""
    G.append([q_near,q_new])

    #"""Child is the key, parent is the value in this dictionary"""
    #parents.update(q_new = q_near) 
    

    return q_new

def circle_obstacles(radius, center):
    # circle_pts = []
    # x_range = [center[0]-radius, center[0]+radius]
    # print(x_range)
    # for x in range(x_range[0], x_range[1]+1):
    #     print(x)
    #     y_1 = (np.sqrt(radius**2 - (x-center[0])**2)) + center[1]
    #     y_2 = -(np.sqrt(radius**2 - (x-center[0])**2)) + center[1]
    #     circle_pts.append([x,y_1])
    #     circle_pts.append([x,y_2])
    # print(circle_pts)
    # return circle_pts
    angle = np.linspace(0, 2*np.pi, 150)
    x = radius*np.cos(angle) + center[0]
    y = radius*np.sin(angle) + center[1]
    l = len(x)
    #print(l)
    pt = []
    for i in range(len(x)):
        pt.append([x[i],y[i]])
    return pt
        
G = []        

q_init = [50,50]
delta = 1
K = 50
D = [[0,100],[0,100]]

diction = {1: [0,2], 2: [4,3]}
#print(diction)

# lst = []
# dista = {}
# dist = {1:2, 2:4, 3:1}
# print(dist.items())
# dista = dict(sorted(dist.items(), key=lambda item:item[1]))
# lst = sorted(dist.keys())
# print(dista)


points = [q_init]
node = Graph(q_init, delta, K, D)
#segs = []

cent = [60,60]
circ_pts = circle_obstacles(10,cent)

while node.K > 0:
    q_rand = random_configuration(node.D)
    q_near = nearest_vertex(q_rand, points)
    q_new = new_configuration(q_near, q_rand, node.delta, circ_pts)
    node.K-=1
    #segs.append()
#print(G)


#print(circ_pts)

# for i,val in enumerate(parents):
#     parent_dict = 
# print(parents)

fig, ax = plt.subplots()
ax.set_xlim(node.D[0][0],node.D[0][1])
ax.set_ylim(node.D[1][0],node.D[1][1])
#seg1 = [q_init, (51,50)]
#seg2 = [(43, 44), (22, 60)]
lc = LineCollection(G)
ax.add_collection(lc)
for i in range(len(circ_pts)):
    print(circ_pts[i])
    x_c = circ_pts[i][0]
    y_c = circ_pts[i][1]
    plt.plot(x_c, y_c, 'ro')

plt.show()








