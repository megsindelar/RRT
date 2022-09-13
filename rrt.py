##############################################
#RRT Program
##############################################

from math import dist, hypot
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


class Graph():
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

def nearest_vertex(q_rand, G):
    closestdist = 100
    for i,a in enumerate(G):
        dist = np.sqrt((q_rand[0]-a[0])**2 + (q_rand[1] - a[1])**2)
        if dist < closestdist:
            closestdist = dist
            q_near = G[i]
    return q_near

                    
def new_configuration(q_near, q_rand, delta):
    print(q_rand)
    print(q_near)

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

    """Child is the key, parent is the value in this dictionary"""
    parents.update(q_new = q_near) 

    return q_new
        
        

parents = {}

q_init = [50,50]
delta = 1
K = 50
D = [[0,100],[0,100]]

diction = {1: [0,2], 2: [4,3]}
print(diction)

# lst = []
# dista = {}
# dist = {1:2, 2:4, 3:1}
# print(dist.items())
# dista = dict(sorted(dist.items(), key=lambda item:item[1]))
# lst = sorted(dist.keys())
# print(dista)


G = [q_init]

node = Graph(q_init, delta, K, D)
q_rand = random_configuration(node.D)
#q_near = nearest_vertex(q_rand, G, points)
#q_new = new_configuration(q_near, q_rand, G.delta)



print(q_init)

# fig, ax = plt.subplots()
# ax.set_xlim(node.D[0][0],node.D[0][1])
# ax.set_ylim(node.D[1][0],node.D[1][1])
# seg1 = [q_init, (51,50)]
# seg2 = [(43, 44), (22, 60)]
# lc = LineCollection([seg1, seg2])
# ax.add_collection(lc)
# plt.show()
#plt.axes.Axes.set_xlim()







