# from cs50 import *
from numpy import *


class calculateField:
    def __init__(self, *argv):
        self.input_data = argv

    def check_value(self,input_data):
        if (type(input_data[0]==list)):
            numbers_calculate = [i for i in input_data[0] and input_data[0] if type(
                i) == float and i>0 or type(i) == int and i>0]
        else:
            numbers_calculate = [i for i in input_data and input_data[0] if type(
                i) == float and i > 0 or type(i) == int and i > 0]
        return numbers_calculate
    def check_name(self,input_data):
        if (type(input_data[0] == list)):
            figure_name = figure_name = [i for i in input_data[0] if i == 'circle' or i == 'rectangle' or i == 'square' or i == 'triangle']
        else:
            figure_name = [i for i in input_data if i == 'circle' or i =='rectangle' or i == 'square' or i == 'triangle']
        return figure_name

    def count_field(self):
        number_to_field = calculateField()
        data_to_calculate = number_to_field.check_value(self.input_data)
        figure_name = number_to_field.check_name(self.input_data)
        try:
            if (len(figure_name) == 0):
                print('incorect')
            elif(figure_name[0] == 'circle' and len(self.input_data[0]) == 2):
                # print(type(self.length_of_sides[0]))
                self.field_c = data_to_calculate[0]*2*pi
                print('field  circele is {}'.format(self.field_c))
                return ['circle',self.field_c]
            elif(figure_name[0] == 'rectangle' and len(self.input_data[0]) == 3):
                self.field_r = data_to_calculate[0] * self.input_data[1]
                print('field  rectangle is {}'.format(self.field_r))
                return ['rectangle',self.field_r]
            elif(figure_name[0] == 'square' and len(self.input_data[0]) == 2):
                self.field_s = data_to_calculate[0]**2
                print('field  square is {}'.format(self.field_s))
                return ['square', self.field_s]
            elif(figure_name[0] == 'triangle'and len(self.input_data[0]) == 3):
                # print(data_to_calculate)
                self.field_t = data_to_calculate[0] * data_to_calculate[1]*0.5
                print('field  triangle is {}'.format(self.field_t))
                return ['triangle', self.field_t]
            else:
                print('Entered data are incorrect. Too little or too much data {}  field.'.format(figure_name[0])) 
        except:
            print('Data  is zero or a negative number')

class compareFields:
    def __init__(self,*argv):
        self.input_data=argv

    def compare(self):
        one_figure = calculateField(self.input_data[0][0])
        two_figure=calculateField(self.input_data[0][1])
        one=one_figure.count_field()
        two=two_figure.count_field()

        if (type(one).__name__ != 'NoneType' and type(two).__name__ != 'NoneType'):
        
            if type(one).__name__ != 'NoneType' and one[1] > two[1] and type(one).__name__ != 'NoneType':
                print('The first figure {} has larger field'.format(one[0]))
            elif type(one).__name__ != 'NoneType' and two[1] > one[1] and type(one).__name__ != 'NoneType':
                print('The first figure {} has larger field'.format(two[0]))
            elif type(one).__name__ != 'NoneType' and one[1] == two[1] and type(one).__name__ != 'NoneType':
                print('the boxes of figures are equal')
# one = calculateField('triangle', 0, 0.0, 5.5555)
# two = calculateField(5,0, 'circle', 'triangle')
# one.count_field()
# two.count_field()
check = compareFields([['circle',0,0.5],[0.1,'square']])
check.compare()

