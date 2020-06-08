a = float(input("输入三角形第一个边长"))
b = float(input("输入三角形第二个边长"))
c = float(input("输入三角形第三个边长"))

# 计算半周长

s = (a + b + c)/2

# 计算面积

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("三角形面积为 {0}".format(area))

# 圆的面积
import math

r = float(input("请输入圆的半径"))
def circleArea(r):
  
  print("圆的面积是",math.pi*(r*r))

circleArea(r)