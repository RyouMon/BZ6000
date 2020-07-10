#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用海龟绘图，绘制同心圆。

import turtle


t = turtle.Pen()
t.speed(0)
t.pensize(5)

colors = ["red", "green", "yellow", "black"]

for i in range(10):
    t.penup()
    t.goto(0, -i*20)
    t.pendown()
    t.pencolor(colors[i%4])
    t.circle(100+i*20)

turtle.done()