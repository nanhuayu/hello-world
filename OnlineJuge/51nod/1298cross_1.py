# -*- coding: utf-8 -*-
#2016/10/21
#1298 圆与三角形
'''
给出圆的圆心和半径，以及三角形的三个顶点，问圆同三角形是否相交。
相交输出"Yes"，否则输出"No"。（三角形的面积大于0）。
Input
第1行：一个数T，表示输入的测试数量(1 <= T <= 10000)，之后每4行用来描述一组测试数据。
4-1：三个数，前两个数为圆心的坐标xc, yc，第3个数为圆的半径R。(-3000 <= xc, yc <= 3000, 1 <= R <= 3000）
4-2：2个数，三角形第1个点的坐标。
4-3：2个数，三角形第2个点的坐标。
4-4：2个数，三角形第3个点的坐标。(-3000 <= xi, yi <= 3000）
Output
共T行，对于每组输入数据，相交输出"Yes"，否则输出"No"。
'''
def getline():
    return [int(i) for i in raw_input().split()]

'''
判断:三角是否在圆内
(x-x0)^2 + (y-y0)^2 = r^2
'''
def c_point(r, point):
    res =  point[0]**2 + point[1]**2 - r**2
    if res > 0:return 1
    elif res <0:return -1
    else:return 0

'''
相交条件:
1:OAB/OBA同为锐角
2:圆心O到直线AB距离小于R
两点直线:(x2 - x1)y - x(y2 - y1) - x2y1 + x1y2 = 0
(ax+by+c)^2<r^2*(a^2+b^2)
勾股定理:AB^2 > |OA^2 - OB^2|
(x2 - x1)^2 + (y2 - y1)^2 > |(x - x1)^2 + (y - y1)^2 - (x - x2)^2 - (y - y2)^2|
(x2 - x1)^2 + (y2 - y1)^2 > |x1^2 + y1^2 - x2^2 - y2^2 + 2x(x2 - x1) + 2y(y2 - y1)|
'''
def c_line(r,p1,p2):
    angle1 = (p2[0]-p1[0])**2+(p2[1]-p1[1])**2 
    angle2 = abs(p1[0]**2-p2[0]**2+p1[1]**2-p2[1]**2)
    dist1 = (p1[0]*p2[1]-p2[0]*p1[1])**2
    dist2 = r**2*((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    return angle1 < angle2 or dist1 > dist2

def iscross(r, triangle):
    result = sum([c_point(r,triangle[i]) for i in range(3)])
    if result == -3:return True
    if result > -3 and result < 3:return False
    return c_line(r,triangle[0],triangle[1]) and c_line(r,triangle[1],triangle[2]) and c_line(r,triangle[2],triangle[0])
    
number = int(raw_input())
for i in range(number):
    getcircle = getline()
    gettriangle = [getline() for i in range(3)]
    triangle = [[gettriangle[i][j] - getcircle[j] for j in range(2)] for i in range(3)]
    if iscross(getcircle[2],triangle):print "No"
    else:print "Yes"