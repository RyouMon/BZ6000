#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用海龟绘图。输入多个点，将这些点都两两相连。
import turtle

pen = turtle.Pen()
p = (0, 0), (100, 100), (100, -100), (-100, 100), (-100, -100)


def connect_points(*points):
    for point in points:
        pen.setpos(points[0])
        pen.goto(*point)



if __name__ == '__main__':
    connect_points(*p)
    turtle.done()