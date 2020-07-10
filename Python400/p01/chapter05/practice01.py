#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入三角形三个顶点的坐标，若有效则计算三角形的面积；
# 如坐标无效，则给出提示。
# 使用海伦公式计算
import math


def s_triangle(p1, p2, p3):
    """
    传入三个坐标，如果可以构成三角形则使用海伦公式计算三角形的面积。
    :param p1: 元组或列表
    :param p2: 元组或列表
    :param p3: 元组或列表
    :return: 计算结果
    """
    a = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    b = math.sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
    c = math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
    if (a + b > c) and (a + c > b) and (b + c > a):
        p = (a + b + c)/2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        print("输入坐标无效！")


print(s_triangle((0, 0), (1, 0), (0, 1)))
print(s_triangle((0, 0), (0, 0), (0, 1)))
