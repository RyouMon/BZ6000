#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
设计一个名为 MyRectangle 的矩形类来表示矩形。这个类包含

(1) 左上角顶点的坐标：x，y

(2) 宽度和高度：width、height

(3) 构造方法：传入 x，y，width，height。如果（x，y）不传则默认是 0，如果 width和 height 不传，则默认是 100.

(4) 定义一个 getArea() 计算面积的方法

(5) 定义一个 getPerimeter()，计算周长的方法

(6) 定义一个 draw()方法，使用海龟绘图绘制出这个
"""
import turtle


class MyRectangle:
    def __init__(self, x=0, y=0, width=100, height=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.height + self.width)

    def draw(self, pen):
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        for i in range(2):
            pen.forward(self.width)
            pen.right(90)
            pen.forward(self.height)
            pen.right(90)


if __name__ == '__main__':
    pen = turtle.Pen()
    r1 = MyRectangle()
    r2 = MyRectangle(0, 100, 100, 90)
    print("矩形1的周长为{0}，面积为{0}。".format(r1.getArea(), r1.getPerimeter()))
    print("矩形2的周长为{0}，面积为{0}。".format(r2.getArea(), r2.getPerimeter()))
    r1.draw(pen)
    r2.draw(pen)
    turtle.done()