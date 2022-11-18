# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         SAM KINNARD
# Section:      565
# Assignment:   Lab 12.16
# Date:         17/11/2022

# importing numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# initializing variables
point_v = np.array([(0),(1)])
x = np.array([0])
y = np.array([1])
matrix = np.array([(1.01, 0.09), (-0.09, 1.01)])

# for loop that multiplies the point by the matrix
# and then the product by the matrix 200 times
for i in range(200):
    prod = point_v @ matrix
    point_v = prod
    x = np.append(x, point_v[0])
    y = np.append(y, point_v[1])
    
# plot of the resulting x and y values with blue dotted line
plt.plot(x,y,'b--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Matrix Multiplication Spiral')
plt.show()