import math
import matplotlib.pyplot as plt
import numpy as np

from bezier_smooth import BezierSmooth
from polynomial_smooth import PolynomialSmooth
from function_smooth import FunctionSmooth

def new_test(x,y,theta):

    # poly=PolynomialSmooth()
    # x,new_route_y,theta=poly.smooth(x,y,theta,4)

    function=FunctionSmooth()
    new_route_x,new_route_y,theta=function.smooth(route_x=x,route_y=y,route_theta=theta)

    bezier_smooth=BezierSmooth(x,y,theta)
    new_route_x,new_route_y,theta=bezier_smooth.smooth()

    new_route_theta=theta

    for i in range(len(new_route_x)):
        print(new_route_x[i],new_route_y[i],new_route_theta[i]*180/math.pi)



    plot1=plt.plot(x, y, '*',label='original values')
    plot2=plt.plot(new_route_x, new_route_y, 'r',label='polyfit values')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.legend(loc=4) # 指定legend的位置,读者可以自己help它的用法
    plt.title('polyfitting')
    plt.show()


def new_test1():
    x = np.arange(1, 17, 1)
    y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
    new_test(x,y,0)

if __name__ == '__main__':
    new_test1()

