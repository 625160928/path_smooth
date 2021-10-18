# path_smooth
通过不同曲线平滑方法平滑路径

目前已有方法为：多项式平滑，指定函数平滑（默认为指数函数平滑），贝塞尔曲线平滑，b样条曲线平滑

## 运行方法


默认运行 `python smooth_main.py`

指定平滑方法在 **smooth_main.py** 的最底下的主程序里有参数，自己改参数

**可选参数列表**：`poly`,`function`,`bezier`,`bspline`

不过因为头文件含有一些carla/ros的msg引用，可能没配置carla的无法直接运行

只需要注释掉msg 的import就好了

## 运行效果
### 多项式曲线优化

### 指定函数曲线优化

### 贝塞尔曲线优化

### b样条曲线优化



