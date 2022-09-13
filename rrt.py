##############################################
#RRT Program
##############################################

import matplotlib as mplt
import numpy as np


class RRT():
    def __init__(self,q_init, delta, K, D):
        self.q_init = [50,50]
        self.delta = 1
        self.K = 50
        self.D = [[0,100],[0,100]]

    def random_configuration(self, D):
        x = np.random.randint(D[0][0], D[0][1])
        #y = 

    #def nearest_vertex(self, q_rand, G):


    #def new_configuration(self, q_near, q_rand, delta):


E = [[0,100],[30,200]]
c = E[0][1]
t = np.random.randint(E[0][0],E[0][1])
print(c)
print(t)