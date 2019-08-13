from cs50 import get_int
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --------------------------------------------TASK 1------------------------

class numberClass:
    def __init__(self):
        self.number = get_int("Give me intiger number:")
    
    def get_number(self):
        return self.number 

def find ():
    while 1:
        first_number = numberClass()
        second_number = numberClass()
        start=first_number.get_number()
        stop=second_number.get_number()

        if (start<stop):
            for i in range(start,stop+1):
                for j in range (start,stop+1):
                    if (j>0 and i >=0):
                        if(i%j==0 and i%2==0 and j%2==0 ):
                            print('{} is divisible by {} and {} & {} are even'.format(j,i,i,j))
        elif(stop<start):
            for i in range(stop, start+1):
                for j in range(stop, start+1):
                   if (j > 0 and i >= 0):
                        if(i % j == 0 and i % 2 == 0 and j % 2 == 0):
                            print('{} is divisible by {} and {} & {} are even'.format(j, i, i, j))
                    
find()


# --------------------------------------------TASK 2------------------------
class circleClass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
     
    def perimeter_field(self):
        try:
            float(self.x)
            float(self.y)
            if(self.x>0 and self.y>0):
                a, self.perimeter_x, self.field_x, self.perimeter_y, self.field_y = lambda x,y : a, 2 * np.pi*self.x, (np.pi*self.x)**2,np.pi*self.y, (np.pi*self.y)**2  
                return 'permiter for x: {}, field for x: {},permiter for y: {}, field for y: {}'\
                .format(self.perimeter_x, self.field_x, self.perimeter_y, self.field_y)
            elif(self.x<0 and self.y>0 ):
                a, self.perimeter_y, self.field_y = lambda y, : a, 2 * \
                np.pi*self.y, (np.pi*self.y)**2
                return 'permiter for y: {}, field for y: {}, x is negative'.format \
                (self.perimeter_y, self.field_y)
            elif(self.y<0 and self.x>0):
                a,self.perimeter_x, self.field_x = lambda x, : a, 2 * \
                np.pi*self.x, (np.pi*self.x)**2
                return 'permiter for x: {}, field for x: {} y is negative'.format \
                (self.perimeter_x, self.field_x)
            elif(self.x<0 and self.y<0):
                return 'The field and permiter cannot be calculated from a negative number'
            else:
                return ' you gave 0'

        except ValueError:
            print("Argument x and y is not a number")
            return '' 

# a = circleClass(1.5,0)
# print(a.perimeter_field())

# --------------------------------------------TASK 3------------------------

class divisibleClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def check_divisible(self):
        try:
            if (self.y ==0):
                return ('You can not  divisible by 0')
            else:
                float(self.x)
                float(self.y)
                return ('X is divisible by Y') if self.x % self.y == 0 else  ('X is not divisible by Y')
        except ValueError:
            print("Argument x and y is not a number")
            return ''
# --------------------------------------------TASK 4------------------------
    def round_number(self):
        try:
            if (self.y == 0):
                return ('You can not  divisible by 0')
            else:
                float(self.x)
                float(self.y)
                self.r_number=round((self.x / self.y),2)
                # print(self.r_number)
                if (self.r_number==-0.0):
                    return 0
                else:
                    return '{}' .format(self.r_number)
        except ValueError:
            print("Argument x and y is not a number")
            return ''

# a=divisibleClass(1,5)
# print(a.round_number()

# --------------------------------------------TASK 5------------------------
class chartClass:
    def __init__(self):
        self.number = get_int("Give me intiger number:")
    
    def draw_chart(self):
        self.x_knots = np.linspace(-3*np.pi,3*np.pi,201)
        self.y_knots = np.linspace(-3*np.pi,3*np.pi,201)
        self.X, self.Y = np.meshgrid(self.x_knots, self.y_knots)
        self.R = np.sqrt((self.X**2+self.Y**2)**4)
        self.Z = np.cos(self.R)**2*np.exp(-0.0008*self.R)
        self.ax = Axes3D(plt.figure(figsize=(8,5)))
        self.ax.plot_surface(self.X, self.Y, self.Z, rstride=5, cstride=5, cmap=plt.cm.coolwarm, linewidth=1.4)
        plt.show()
        return ''

# b=chartClass()
# b.draw_chart()
