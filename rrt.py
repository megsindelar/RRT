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
    for a in points:
        distance = {}
        diff = abs(np.subtract(a,q_rand))
        print(diff)
        distance.update(a = diff)

    #print(distance)
    dist = dict(sorted(distance.items(), key=lambda item:item[1]))
    #print(dist)
    q_near = list(dist.keys())[0]
    print(q_near)
    return q_near
                    
def new_configuration(q_near, q_rand, delta):
    print(q_rand)
    print(q_near)
    m = (q_rand[1]-q_near[1])/(q_rand[0]-q_near[0])

    theta1 = np.atan(q_rand[0]-q_near[0])/(q_rand[1]-q_near[1])
    theta2 = np.atan(q_rand[1]-q_near[1])/(q_rand[0]-q_near[0])
    theta = [theta1, theta2]
    theta.sort()
    if theta[0] == theta1:
        theta_real = theta1
        theta1_true = 1
    else:
        theta_real = theta2
        theta1_true = 0

    adj = abs(delta*np.cos(theta_real))
    acr = abs(delta*np.sin(theta_real))

    if theta1_true == 1 and q_near[0] > 0 and q_near[1] > 0:
        """First quadrant, theta1"""
        x_new = q_near[0] + acr
        y_new = q_near[1] + adj

    elif theta1_true == 0 and q_near[0] > 0 and q_near[1] > 0:
        """First quadrant, theta2"""
        x_new = q_near[0] + adj
        y_new = q_near[1] + acr    

    elif theta1_true == 1 and q_near[0] < 0 and q_near[1] > 0:
        """Second quadrant, theta1"""
        x_new = q_near[0] - acr
        y_new = q_near[1] + adj

    elif theta1_true == 0 and q_near[0] < 0 and q_near[1] > 0:
        """Second quadrant, theta2"""
        x_new = q_near[0] - adj
        y_new = q_near[1] + acr

    elif theta1_true == 1 and q_near[0] < 0 and q_near[1] < 0:
        """Third quadrant, theta1"""
        x_new = q_near[0] - acr
        y_new = q_near[1] - adj

    elif theta1_true == 0 and q_near[0] < 0 and q_near[1] < 0:
        """Third quadrant, theta2"""
        x_new = q_near[0] - adj
        y_new = q_near[1] - acr

    elif theta1_true == 1 and q_near[0] > 0 and q_near[1] < 0:
        """Fourth quadrant, theta1"""
        x_new = q_near[0] + acr
        y_new = q_near[1] - adj

    elif theta1_true == 0 and q_near[0] < 0 and q_near[1] < 0:
        """Second quadrant, theta2"""
        x_new = q_near[0] + adj
        y_new = q_near[1] - acr

    q_new = [x_new, y_new]

    points.append(q_new)

    """Child is the key, parent is the value in this dictionary"""
    parents.update(q_new = q_near) 

    return q_new
        
    
        

parents = {}

q_init = (50,50)
delta = 1
K = 50
D = [[0,100],[0,100]]


# lst = []
# dista = {}
# dist = {1:2, 2:4, 3:1}
# print(dist.items())
# dista = dict(sorted(dist.items(), key=lambda item:item[1]))
# lst = sorted(dist.keys())
# print(dista)


points = [q_init]


G = Graph(q_init, delta, K, D)
q_rand = random_configuration(G.D)
q_near = nearest_vertex(q_rand, G)
#q_new = new_configuration(q_near, q_rand, G.delta)



print(q_init)

fig, ax = plt.subplots()
ax.set_xlim(G.D[0][0],G.D[0][1])
ax.set_ylim(G.D[1][0],G.D[1][1])
seg1 = [q_init, (51,50)]
seg2 = [(43, 44), (22, 60)]
lc = LineCollection([seg1, seg2])
ax.add_collection(lc)
plt.show()
#plt.axes.Axes.set_xlim()

