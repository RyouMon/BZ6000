#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 绘制四个矩形
import turtle


def draw_rectangle(x, y, w=100, h=80):
    """
    以某个坐标为顶点绘制一个特定大小的矩形
    :param x: 横坐标
    :param y: 纵坐标
    :param w: 矩形的宽度
    :param h: 矩形的高度
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)


if __name__ == '__main__':
    turtle.pensize(5)
    turtle.color("red")
    draw_rectangle(0, 0)
    draw_rectangle(0, 100)
    draw_rectangle(120, 0)
    draw_rectangle(120, 100)
