## functions for linear regression
import matplotlib.pyplot as plt
import numpy as np
def delta(x):
    val1 = 0
    val2 = 0
    for i in range(len(x)):
        val1 += x[i]**2
        val2 += x[i]
    return val1*len(x)-val2**2

def slope(x, y):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(len(x)):
        sum1+= x[i]*y[i]
        sum2 += x[i]
        sum3 += y[i]
    return (len(x)*sum1-sum2*sum3)/delta(x)

def intercept(x,y):
    sum1 = 0
    sum2 = 0
    for i in range(len(x)):
        sum1+=y[i]
        sum2+=slope(x,y)*x[i]
    return (sum1-sum2)/len(x)

def square_s(x,y):
    sum = 0
    for i in range(len(x)):
        sum +=(y[i]-slope(x,y)*x[i]-intercept(x,y))**2
    return sum/(len(x)-2)

def sb(x,y):
    return np.sqrt(len(x)*square_s(x,y)/delta(x))

def sm(x,y):
    sum = 0
    for i in range(len(x)):
        sum+=x[i]**2
    return np.sqrt(square_s(x,y)*sum/delta(x))
