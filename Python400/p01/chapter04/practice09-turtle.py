#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用海龟绘图，绘制 18*18 的棋盘。
import turtle


t = turtle.Pen()
t.speed(0)

for i in range(18):
    t.goto(340, -i*20)
    t.penup()
    t.goto(0, -(i+1)*20)
    t.pendown()

for i in range(18):
    t.penup()
    t.goto(i * 20, 0)
    t.pendown()
    t.goto(i * 20, -340)

turtle.done()