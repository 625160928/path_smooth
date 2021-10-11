import math
from scipy.optimize import curve_fit
import numpy as np

def function1(x,a,b):
    return a*np.exp(b/x)

# 使用非线性最小二乘法拟合
#https://www.cnblogs.com/jingsupo/p/python_curve_fit.html

class FunctionSmooth():

    def smooth(self,route_x,route_y,route_theta,func=function1):
        popt, pcov = curve_fit(func, route_x,route_y)
        a=popt[0] # popt里面是拟合系数，读者可以自己help其用法
        b=popt[1]
        yvals=func(route_x,a,b)
        new_route_theta=[]
        for i in route_x:
            dx=0.001
            dy=func(i+dx,a,b)-func(i,a,b)
            new_route_theta.append(math.atan2(dy,dx))
        return route_x,yvals,new_route_theta

