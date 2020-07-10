#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
使用海龟绘图。输入多个点，将这些点都两两相连。
"""
import turtle

pen = turtle.Pen()


def connect_points(*p):
    for i in range(len(p)):
        for point in p[i+1:]:
            pen.setpos(p[i])
            pen.goto(*point)


points = (0, 0), (100, 100), (100, -100), (-100, 100), (-100, -100), (0, 150), (0, -150), (150, 0), (-150, 0)
connect_points(*points)
turtle.done()

