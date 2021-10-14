import math
import matplotlib.pyplot as plt
import numpy as np
import tf

from nav_msgs.msg import Path, Odometry
from carla_nav_msgs.msg import Path as PathArray
from geometry_msgs.msg import Pose, PoseStamped

from .bezier_smooth import BezierSmooth
from .polynomial_smooth import PolynomialSmooth
from .function_smooth import FunctionSmooth
from .b_spline_smooth import BSplineSmooth

def path_smooth(path:PathArray):
    for i in range(len(path.paths)):
        x_arr=[]
        y_arr=[]
        theta_arr=[]
        for pose in path.paths[i].poses:
            x=pose.pose.position.x
            y=pose.pose.position.y
            (_, _, theta) = tf.transformations.euler_from_quaternion(
                [pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w])
            x_arr.append(x)
            y_arr.append(y)
            theta_arr.append(theta)
            # print(x,y,theta*180/math.pi)
        new_route_x,new_route_y,new_route_theta=smooth(x_arr,y_arr,theta_arr,method='bezier')
        path.paths[i].poses=route_to_formal_path(new_route_x,new_route_y,new_route_theta)
    return path

def route_to_formal_path( route_x, route_y, route_theta):
    type_route = Path()
    for i in range(len(route_x)):
        tmp_pose = PoseStamped()
        tmp_pose.pose.position.x = route_x[i]
        tmp_pose.pose.position.y = route_y[i]

        q = tf.transformations.quaternion_from_euler(0, 0, route_theta[i])
        tmp_pose.pose.orientation.x = q[0]
        tmp_pose.pose.orientation.y = q[1]
        tmp_pose.pose.orientation.z = q[2]
        tmp_pose.pose.orientation.w = q[3]
        # type_route.append(tmp_pose)

        type_route.poses.append(tmp_pose)
    return type_route


def smooth(x,y,theta,method='poly'):
    new_route_x, new_route_y, new_route_theta=None,None,None
    if method=='poly':
        new_route_x,new_route_y,new_route_theta=PolynomialSmooth().smooth(x,y,theta,4)
    if method=='function':
        new_route_x,new_route_y,new_route_theta=FunctionSmooth().smooth(route_x=x,route_y=y,route_theta=theta)
    if method=='bezier':
        new_route_x,new_route_y,new_route_theta=BezierSmooth(x,y,theta).smooth()
    if method=='bspline':
        new_route_x,new_route_y,new_route_theta=BSplineSmooth().smooth(x,y,theta,k=3)
    return new_route_x,new_route_y,new_route_theta

def new_test(x,y,theta,method='poly'):

    new_route_x,new_route_y,new_route_theta=smooth(x,y,theta,method)

    for i in range(len(new_route_x)):
        print(new_route_x[i],new_route_y[i],new_route_theta[i])



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
    theta = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
    new_test(x,y,theta,method='bezier')

if __name__ == '__main__':
    new_test1()

