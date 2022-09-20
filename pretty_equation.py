# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         SAM KINNARD
#               Caleb Lorimor
#               Ryan Kethley
#               Evan Slyter
# Section:      565
# Assignment:   Lab 4.14
# Date:         15/9/2022

from math import *

A = float(input('Please enter the coefficient A: '))
B = float(input('Please enter the coefficient B: '))
C = float(input('Please enter the coefficient C: '))

# every scenario for A coefficient
if A == 1:
    print('The quadratic equation is x^2 ',end='',sep='')
elif A == -1:
    print('The quadratic equation is - x^2 ',end='',sep='')
elif A > 0:
    print('The quadratic equation is ', int(A),'x^2 ',end='', sep='')
elif A < 0:
    print('The quadratic equation is - ',int(-1*A),'x^2 ',end='',sep='')
elif A == 0:
    print('The quadratic equation is ',end='',sep=' ')
    
# every scenario for the B coefficient
if B == 1:
    print('+ x',end='',sep='')
elif B == -1:
    print('- x ',end='',sep='')
elif B > 0:
    if A == 0:
        print(int(B),'x ',end='', sep='')
    else:
        print('+ ', int(B),'x ',end='', sep='')
elif B < 0:
    print('- ',int(-1*B),'x ',end='',sep='')
elif B == 0:
    print('',end='',sep='')
    
# every scenario for the C coefficient
if C == 1:
    print('+ 1 ',end='',sep='')
elif C == -1:
    print('- 1',end='',sep='')
elif C > 0:
    print('+ ', int(C),end='', sep='')
elif C < 0:
    print('- ',int(-1*C),end='',sep='')
elif C == 0:
    print('',end='',sep='')
    
print(' = 0')
    
