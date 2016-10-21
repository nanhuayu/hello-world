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

def readline():
    getcircle = []
    gettriangle = [[],[],[]]
    getcircle = raw_input().split()
    gettriangle[0] = raw_input().split()
    gettriangle[1] = raw_input().split()
    gettriangle[2] = raw_input().split()
    #print getcircle
    #print gettriangle
    return getcircle,gettriangle

def guess(circle, tri):
    return int((float(tri[0]) - float(circle[0]))**2 + (float(tri[1]) - float(circle[1]))**2 - float(circle[2])**2)

def cross(circle, triangle):
    result = [0,0,0]
    for i in range(3):
        result[i] = guess(circle,triangle[i])
        if not result[i]:return False
    return abs(sum(result)) == sum([abs(i) for i in result])
    
number = int(raw_input())
for i in range(number):
    circle, triangle = readline()
    if cross(circle,triangle):print "No"
    else:print "Yes"