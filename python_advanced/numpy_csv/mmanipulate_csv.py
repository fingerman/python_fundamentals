from numpy import genfromtxt
import numpy as np

my_data = genfromtxt('test.csv', delimiter=',')
print(my_data)
print(type(my_data))
print()
print()

#exchange first and last row
my_data1 = my_data.copy()
my_data1[0, :] = my_data[2, :]
my_data1[2, :] = my_data[0, :]
print(my_data1)

