import numpy as np
from numpy.random import *
from matplotlib.pyplot import *
from sys import argv



# -------------------------------------------------------------LAB 1----------------------------------------------

#1---------------------------------------------------------TASK WITH  FUNCTION------------------------------------------------
def quadratic_function():                                                                         #  calculation of a quadratic function
    #  print([2*x**2+2*x+2  for x in (range(56,101))])
     print('Values of function: y = 2x^2 + 2x + 2')
     for x in range(56,101):
        y=2*x**2+2*x+2
        print('argument x:{:-1}, function value y:{:-1}' .format(x,y))



# quadratic_function()



#2----------------------------------------------------------TASK WITH  FACTORIAL------------------------------------------------
def factorial():                                                                                  #calculating the factorial from the number 
    while 1:
            try:                                                                                     #exception for integer number     
                print('Give me a intiger number: ')
                number=input()                                                                                    
                if  number == 'end':                                                                 #the exit from loop while
                    break 
                else:
                    number=int(float(number))                                                          
                    one=1
                    if number == 0:
                        print('Factorial of {:-1} is {:-1} .'.format(number,1))
                    elif number  < 0:
                    	print('Factorial of {:-1} not exist .'.format(number))
                    else:
                        for x in range(number):
                            two=x+1
                            one=one*two
                            score=one
                        print('Factorial of {:-1} is {:-1} .'.format(number,score))
            except ValueError:
                print('This is not a intiger number')                                               #exception notice

# factorial()


#3----------------------------------------------------------TASK WITH  FACTORIAL------------------------------------------------

def min_value(array_of):
	value_index=[]                                                                           #searching for min and index values
	min_number=min(array_of)                                                                        
	print('Min number from array is {:-1}'.format(min_number))
	for i in range(len(array_of)):
		if min_number==array_of[i]:
			value_index.append(i)
			# print('Index min number is: {:-1}'.format(i))
	print('Index for min value:',value_index)
example_array=[-5,-9,0,4,-9,-9,-9]
# min_value(example_array)


#4----------------------------------------------------------TASK WITH  CHART------------------------------------------------
def function_chart():
    while 1:
        try:
            if len(argv) == 2:
               
                print('The input is:', argv[1])
                input_f=(int(round(float(argv[1]))))
                plot([x*x+2 for x in range(1,input_f)])
                show()
                break
               
            else:
                print('No input')

            
            # list_input=input_f.split(',')

            
            # plot([int(x) for x in list_input ])
            # show()
            
            break
        except ValueError:
            print('This is not a intiger  number')
            break
function_chart()
