
#Jacob Silveira
#CST-305
#10/2/2022

#needed packages
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math
#for recording the runtime
import timeit

#define IVP
t0 = 0
x0 = 1
y0 = 5
h = 0.02
Sol = 0
Table = np.array([x0,y0,Sol])
#print out starting value and method
print("Runge Kutta Method for ODE")
print("")
print("-------------------------------")

print ("n | x{n} | y{n} | k1 | k2 | k3 | k4 | y{n+1}")
print("-------------------------------")
#the ODE that will be solved is 
#y' = y / (e^x -1)
def equation(y,t):
    dydx = y/(math.exp(1)-1)
    return dydx
#plugs numbers into equation
def input(x, y):
    yPrime = y/( math.exp(x)-1)
    return yPrime

def RKF(x,y,h):
    #to figure the intial values needed
    k1 = h * input(x,y)
    k2 = h * input(x+h/2, y + k1/2)
    k3 = h * input(x+h/2, y + k2/2)
    k4 = h * input(x+h,y + k3)
    nextY = y + 1/6 * (k1+2*k2+2*k3+k4)
    #then print table
    print("------------------Using Runge Kutta Method-------------------------")
    print("evaluated to n = 5")
    print("")
    #initial values
    n=1
    nextY = y + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    print("0", " | ", x, " | ", y, " | ", k1,  " | ", k2, " | ", k3, " | ", k4, " | ", nextY)
    print("")

    #putting in the while loop
    while (n < 6):
        #first calc x and y to continue with the problem 
        x = x + h
        y = y + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        #then calc k1,k2,k3,k4
        k1 = h * input(x,y)
        k2 = h * input(x+h/2, y+k1/2)
        k3 = h * input(x+h/2, y+k2/2)
        k4 = h * input(x+h, y+k3)
        nextY = y + 1/6 * (k1+2*k2+2*k3+k4)
        #and print values
        print(n, " | ", x, " | ", y, " | ", k1,  " | ", k2, " | ", k3, " | ", k4, " | ", nextY)
        print("")
        n = n + 1

RKF(x0,y0,h)

#start a runtime timer 
start = timeit.default_timer()

t = np.linspace(0,1000) #for num of solution needed
y = odeint(equation,y0,t)

print("-----data values-----")
print("using ODIENT")
print(y)

#plot and label graph
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

#stop runtime
stop = timeit.default_timer()

#print time to execute code
print("")
print("----------------------------------------")
print("Calculated time to execute code is -->")
print('Time: ', stop-start)  
print("Complexity: O(n^2)") 

