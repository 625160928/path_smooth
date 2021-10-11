import matplotlib.pyplot as plt
import numpy as np

class BSplineSmooth():
    def __init__(self):
        self.node_number=1000

    # 计算基函数，i为控制顶点序号，k为次数，u为代入的值，NodeVector为节点向量
    # 该函数返回第i+1个k次基函数在u处的值
    def b_spline_basis(self,i, k, u, nodeVector):
        # nodeVector = np.mat(nodeVector)  # 将输入的节点转化成能够计算的数组
        # k=0时，定义一次基函数
        if k == 0:
            if (nodeVector[i] < u) & (u <= nodeVector[i + 1]):  # 若u在两个节点之间，函数之为1，否则为0
                result = 1
            else:
                result = 0
        else:
            # 计算支撑区间长度
            length1 = nodeVector[i + k] - nodeVector[i]
            length2 = nodeVector[i + k + 1] - nodeVector[i + 1]
            # 定义基函数中的两个系数
            if length1 == 0:  # 特别定义 0/0 = 0
                alpha = 0
            else:
                alpha = (u - nodeVector[i]) / length1
            if length2 == 0:
                beta = 0
            else:
                beta = (nodeVector[i + k + 1] - u) / length2
            # 递归定义
            result = alpha * self.b_spline_basis(i, k - 1, u, nodeVector) + beta * self.b_spline_basis(i + 1, k - 1, u,
                                                                                             nodeVector)
        return result

    def get_b_spline(self,X,Y,THETA,k,nodeVector):
        n = len(X)
        basis_i = np.zeros( self.node_number)  # 存放第i个基函数
        rx = np.zeros( self.node_number)  # 存放B样条的横坐标
        ry = np.zeros( self.node_number)
        rtheta = np.zeros( self.node_number)
        for i in range(n):  # 计算第i个B样条基函数，
            U = np.linspace(nodeVector[k], nodeVector[n], self.node_number)  # 在节点向量收尾之间取100个点，u在这些点中取值
            j = 0
            for u in U:
                nodeVector = np.array(nodeVector)
                basis_i[j] = self.b_spline_basis(i, k, u, nodeVector)  # 计算取u时的基函数的值
                j = j + 1
            rx = rx + X[i] * basis_i
            ry = ry + Y[i] * basis_i
            rtheta = rtheta + THETA[i] * basis_i
        return rx,ry, rtheta

    # 画B样条函数图像
    def smooth(self, X, Y,THETA, k):
        # draw_px()

        n = len(X)
        p = k
        if n + k + 1 - p * 2 > 0:
            nodeVector = np.linspace(0, 1, n + k + 1 - p * 2)
            y = []
            for i in range(p):
                y.append(0)
            y += nodeVector.tolist()
            for i in range(p):
                y.append(1)
            nodeVector = np.array(y)
        else:
            nodeVector = np.linspace(0, 1, n + k + 1)


        rx,ry, rtheta=self.get_b_spline(X,Y,THETA,k,nodeVector)

        return rx, ry, rtheta


if __name__ == '__main__':
    k = 3
    # nodeVector = [0, 0,1, 1,2, 2, 3, 4, 5, 5, 5]
    X = [0, 2, 2, 3, 4, 5, 6]
    Y = [0, 3, 1, 3, 1, 4, 0]
    theta = [0, 3, 1, 3, 1, 4, 0]

    x,y,theta=BSplineSmooth().smooth(X,Y,theta,k=3)

    plt.plot(x,y)
    plt.show()
    print(x,y,theta)


