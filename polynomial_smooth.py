import math

import matplotlib.pyplot as plt
import numpy as np

#https://www.cnblogs.com/jingsupo/p/python_curve_fit.html
class PolynomialSmooth():
    def fit(self,route_x,route_y,polynomial_times=3):
        z1 = np.polyfit(route_x,route_y,polynomial_times) # 用polynomial_times次多项式拟合
        p1 = np.poly1d(z1)
        return p1

    def smooth(self,route_x,route_y,route_theta=None,polynomial_times=3):
        p1=self.fit(route_x, route_y,polynomial_times=polynomial_times)
        new_route_y=p1(route_x)
        theta_p=p1.deriv(1)
        dy=theta_p(route_x)
        new_route_theta=[]
        for i in dy:
            new_route_theta.append(math.atan2(i,1))
        return route_x,new_route_y,new_route_theta
