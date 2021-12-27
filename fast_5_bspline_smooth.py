import matplotlib.pyplot as plt
import numpy as np

class Fast5BSplineSmooth():
    def __init__(self):
        self.node_number=1000

    # 画B样条函数图像
    def smooth(self, X, Y,THETA):
        points=[]
        for i in range(len(X)):
            points.append([X[i],Y[i],THETA[i]])
        np_points=np.array(points)
        if len(X)<5:
            return X, Y,THETA
        ans_points=np.zeros(np_points.shape,np.float)
        ans_points[0]=(69*np_points[0]+ 4.0 * np_points[1] - 6.0 * np_points[2] + 4.0 * np_points[3] - np_points[4])/70
        ans_points[1] =(2.0 * np_points[0] + 27.0 * np_points[1] + 12.0 * np_points[2] - 8.0 * np_points[3] + 2.0 * np_points[4]) / 35.0
        N=len(X)
        for i in range(2,len(X)-2):
            ans_points[i]=(-3.0 * (np_points[i - 2] + np_points[i + 2])+ 12.0 * (np_points[i - 1] + np_points[i + 1]) + 17.0 * np_points[i] ) / 35.0

        ans_points[N - 2] = (2.0 * np_points [N - 5] - 8.0 * np_points [N - 4] + 12.0 * np_points[N - 3] + 27.0 * np_points[N - 2] + 2.0 *np_points [
            N - 1]) / 35.0
        ans_points[N- 1] = (- np_points [N - 5] + 4.0 * np_points[N - 4] - 6.0 * np_points[N - 3] + 4.0 * np_points[N - 2] + 69.0 *np_points[N - 1]) / 70.0;
        rx=[]
        ry=[]
        rtheta=[]
        for i in range(len(ans_points)):
            rx.append(ans_points[i][0])
            ry.append(ans_points[i][1])
            rtheta.append(ans_points[i][2])
            print(ans_points[i])
        return rx,ry,rtheta

if __name__ == '__main__':
    # k = 3
    # # nodeVector = [0, 0,1, 1,2, 2, 3, 4, 5, 5, 5]
    # X = [0, 2, 2, 3, 4, 5, 6]
    # Y = [0, 3, 1, 3, 1, 4, 0]
    # theta = [0, 3, 1, 3, 1, 4, 0]
    #
    # x,y,theta=BSplineSmooth().smooth(X,Y,theta,k=3)
    #
    # plt.plot(x,y)
    # plt.show()
    # print(x,y,theta)


    import time
    msg=[(0.023343324661254883, 0.40249213576316833, 0.01015827189894546)
,(0.804, 0.1638, -0.039900000000000005)
,(1.9219, 0.1121, -0.04000000000000001)
,(3.1387, 0.0586, -0.0401)
,(4.3607, 0.0425, -0.04080000000000001)
,(5.4492, -0.0262, -0.0393)
,(6.4633, -0.0596, -0.0393)
,(7.6847, -0.107, -0.0398)
,(8.91, -0.1696, -0.041)
,(10.0715, -0.2107, -0.040200000000000014)
,(11.2034, -0.2681, -0.036)
,(12.4118, -0.2748, -0.017299999999999996)
,(13.6274, -0.2894, 0.0039000000000000003)
,(14.8548, -0.2883, 0.006900000000000001)
,(16.0539, -0.2652, 0.0053)
,(17.0887, -0.276, 0.0044)
,(18.1375, -0.2627, 0.005600000000000001)
,(19.1646, -0.2807, -0.006000000000000001)
,(20.2331, -0.2588, -0.0012000000000000001)
,(21.2543, -0.2902, 0.039400000000000004)
,(22.3092, -0.2342, 0.10910000000000002)
,(23.3351, -0.0999, 0.21820000000000003)
,(24.59, 0.2469, 0.4136)
,(25.7115, 0.8472, 0.6147)
,(26.5982, 1.483, 0.6307999999999999)
,(27.5441, 2.1847, 0.6370000000000001)
,(28.5955, 2.9568, 0.6877)
,(29.6511, 3.8573, 0.7897000000000002)
,(30.6667, 4.9372, 0.9361000000000002)
,(31.2972, 5.7273, 1.0617000000000003)
,(31.8245, 6.6607, 1.2120000000000002)
,(32.2281, 7.5968, 1.3799)
,(32.5187, 8.6331, 1.5636000000000003)
,(32.6179, 9.6339, 1.7546000000000004)
,(32.5057, 10.6519, 1.8696000000000004)
,(32.0828, 12.0499, 1.8465000000000005)
,(31.8099, 13.0312, 1.7830000000000001)
,(31.5555, 14.0211, 1.6921999999999997)
,(31.3966, 15.5611, 1.5430000000000001)
,(31.4328, 16.6439, 1.5211)
,(31.4728, 17.6992, 1.5047000000000004)
,(31.5579, 18.77, 1.4992)
,(31.6468, 19.8713, 1.5001)
,(31.7098, 21.0067, 1.4998000000000002)
,(31.8203, 22.1415, 1.4998999999999998)
,(31.8742, 23.396, 1.5001)
,(31.9859, 24.6115, 1.5009000000000003)
,(32.0757, 25.9033, 1.5006000000000002)
,(32.1562, 27.2401, 1.5215000000000003)
,(32.2431, 28.5788, 1.5721)
,(32.2627, 29.9663, 1.5931000000000002)
,(32.2463, 31.4074, 1.5967000000000002)
,(32.2024, 32.8435, 1.5987000000000002)
,(32.1461, 34.3792, 1.5980000000000003)
,(32.1256, 35.8963, 1.6043000000000005)
,(32.0896, 37.4899, 1.6464000000000003)
,(31.9964, 39.1478, 1.6912000000000003)
,(31.7928, 40.7313, 1.7046000000000001)
,(31.5931, 42.4419, 1.7213000000000005)
,(31.357, 44.129, 1.7236000000000002)
,(31.0784, 45.8669, 1.6876000000000002)
,(30.8606, 47.5696, 1.6265000000000005)
,(30.7167, 49.4171, 1.5967000000000002)
,(30.6162, 51.2194, 1.5869)
,(30.5673, 53.1088, 1.5851000000000004)
,(30.5361, 55.0008, 1.586)
,(30.4974, 56.8767, 1.6052999999999997)
,(30.4579, 58.7123, 1.6316000000000002)
,(30.4093, 60.3659, 1.6635)
,(30.3511, 61.9255, 1.6953999999999998)
,(30.2808, 63.2896, 1.7256)
,(30.1861, 64.4872, 1.7587000000000004)
,(30.1008, 65.5186, 1.8077)
,(29.9488, 66.8138, 1.9193000000000002)
,(29.6804, 67.8141, 2.0550000000000006)
,(29.0424, 68.8929, 2.2036),
(28.2415, 69.9383, 2.2150000000000003),
(27.5927, 70.7896, 2.2702),
(26.8585, 71.6607, 2.387),
(25.9644, 72.4689, 2.5433),
(24.8816, 73.1817, 2.7517),
(23.5935, 73.689, 2.8354),
(22.1728, 74.1582, 2.8433),
(21.1927, 74.4634, 2.8781),
(20.1403, 74.7268, 2.9447),
(19.0122, 74.9825, 3.0352),
(17.9167, 75.1481, 3.069),
(16.7626, 75.215, 3.0735),
(15.6538, 75.2954, 3.0747),
(14.5078, 75.3632, 3.0814),
(13.391, 75.4591, 3.1187),
(12.2379, 75.4923, -3.0921),
(11.1074, 75.4175, -3.0239),
(9.8955, 75.3052, -3.0078),
(8.6517, 75.1501, -3.0019),
(7.4058, 74.9875, -2.9991),
(6.16, 74.8291, -2.9911),
(4.9685, 74.6429, -2.9528),
(3.7704, 74.4467, -2.8808),
(2.6532, 74.1498, -2.7697),
(1.621, 73.8197, -2.6338),
]
    xx=[]
    yy=[]
    the=[]
    start_time=time.time()
    for i in msg:
        xx.append(i[0])
        yy.append(i[1])
        the.append(i[2])
    x,y,theta=Fast5BSplineSmooth().smooth(xx, yy, the)
    end_time=time.time()
    print(end_time-start_time)
    plt.clf()
    plt.plot(xx, yy,color='green')
    plt.plot(x,y,color='red')
    plt.show()

