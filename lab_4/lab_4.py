import numpy as np 
import random
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import linspace, cos, exp, random, meshgrid, zeros
from scipy.optimize import fmin
from scipy.optimize import basinhopping

from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
from mpl_toolkits.mplot3d import Axes3D
import math as m
import time

class eulerSchema:
    def __init__(self,T,a,h):
        self.T=T
        self.a=a
        self.h=h  
    # def approximation(funcion_Euler):
    #     def approximation_in(x):
    #         x=funcion_Euler(x)

    #         return x
    #     return approximation_in
    # @approximation
    # def approximation():
        
    def calculating_differential(self):
        try:
            assert self.T > 0 and self.h>0 and self.a>0
            
            self.t=np.arange(0,self.T,self.h)
            self.x=np.ones(self.t.shape)
            for i in range(len(self.t)-1):
                self.x[i+1]=self.x[i]+self.h*(self.a*self.x[i])
            return self.x,self.t
        except AssertionError:
            return('Input data T  or h or a  is negative or zero.  Numbers should be bigger from zero.'),0

    def simulation(self):
        
        x,t=eulerSchema.calculating_differential(self)
        if type(x)==str:
            print(x)
        else:
            plt.plot(t,x,'-g')
            plt.xlabel('t',fontsize=20)
            plt.ylabel('x',fontsize=20)
            plt.show()
            return ""
        
    def approximation(self):
        x,t=eulerSchema.calculating_differential(self)
        if type(x)==str:
            print(x)
        else:
            y = np.zeros(t.shape)
            y[0]=random.randint(0,100)
            for i in range(t.size-1):
                y[i+1] = y[i] + self.h*(self.a*x[i+1])
            
            plt.plot(t,x,'k', label='x')
            plt.plot(t,y,'g', label='y:approximation x')
            plt.xlabel('t', fontsize=14)
            plt.ylabel('state', fontsize=14)
            plt.legend(loc='upper right', fontsize=14)
            plt.show()
       
   


# first_schema=eulerSchema(10,0.5,0.001)

# print(first_schema.simulation())
# print(first_schema.approximation())
# 


# --------------------------------------------------------------TASK4--------------------------------------------------------------
# zeeman model for heartbeat
# T-is the muscle tension and is related to blood pressure (the higher is blood pressure the higher is the muscle tension)
# xo-1 is the average muscle length in the diastole (the period of time when the heart fills with blood after contraction).
def F(x,t):
    xo=1
    T=4
    eps=5
    dx=[0,0]
    dx[0]=x[1]-xo
    dx[1]=-((x[1]**3)-(T*x[1])+x[0])/eps
    # print(dx[0])
    return dx


def main():
    # czesc mateusz magda

    t_min = 0
    t_max = 100
    h = 0.01
    t = np.arange(t_min, t_max+h, h)
    initial_x = ((1,0))
    X = odeint(F, initial_x, t)
    
    plt.figure(1)
    plt.xlabel('t', fontsize=14)
    plt.ylabel('X', fontsize=14)
   
    plt.plot(t,X,)
    
    plt.figure(2)
    plt.plot(X[:,0],X[:,1])
    plt.axis('equal')
    plt.show()
# main()

# ---------------------------------------------------------------Task 5------------------------------------
def f(x):
    
    return m.sin(1+x[0]**2+x[1]**2)+m.cos(x[1]*1.5)


def neg_f(x):
    return -f(x)

def main_optimal():
    x0 = random.randn(2)
    x0_g = random.rand(2)
    start_time = time.time()
    x_min = fmin(neg_f, x0)
    print(type((x_min)))
    delta = 3
    x_glob = basinhopping(neg_f, x0_g)
    stop_time=time.time()
    print('time',stop_time-start_time)
    # print(stop_time-start_time)
    x_glob_p = x_glob['x']
    x_knots = linspace(x_min[0] - delta, x_min[0] + delta, 41)
    y_knots = linspace(x_min[1] - delta, x_min[1] + delta, 41)
    X, Y = meshgrid(x_knots, y_knots)
    Z = zeros(X.shape)
    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            Z[i][j] = f([X[i, j], Y[i, j]])

    ax = Axes3D(figure(figsize=(8, 5)))
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
    ax.plot([x0[0]], [x0[1]], [f(x0)], color='g',marker='o', markersize=20, label='initial')
    ax.plot([x_min[0]], [x_min[1]], [f(x_min)] , color='k',marker='o', markersize=20, label='lokal')
    ax.plot([x_glob['x'][0]], [x_glob['x'][1]],[f(x_glob_p)], color='b', marker='o', markersize=10, label='glob')
            
    ax.legend()
    show()
main_optimal()


def x_glob():
    x0 = random.randn(2)

    x_min=basinhopping(neg_f,x0)
    print(x_min)
# x_glob()

def fun():
     x = random.randn(2)/10
     print(x)
     return((1+x[0]**2+x[1]**2))

def algo_opt():
    opt_min=fun()
    print(opt_min)
    solv=[]
    while opt_min>1:
        opt=fun()
        print(opt)
        # if opt<opt_min:
        #     opt_min=opt
        #     solv.append(opt.min)


# algo_opt()
