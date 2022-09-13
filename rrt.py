##############################################
#RRT Program
##############################################

from math import dist, hypot
import matplotlib.pyplot as plt
import numpy as np


class G():
    def __init__(self,q_init, delta, K, D):
        self.q_init = [50,50]
        self.delta = 1
        self.K = 50
        self.D = [[0,100],[0,100]]
        self.G = [q_init]

    def random_configuration(self, D):
        x = np.random.randint(D[0][0], D[0][1])
        y = np.random.randint(D[1][0], D[1][1])
        q_rand = [x,y]

    def nearest_vertex(self, q_rand, G):
        for a in G:
            distance = {}
            distance.update(a = abs(np.subtract(a,q_rand)))
        dict(sorted(distance.item(), key=lambda item:item[1]))
        q_near = list(distance.keys())[0]
                    
    def new_configuration(self, q_near, q_rand, delta):
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

        
plt.axes.Axes.set_xlim()

