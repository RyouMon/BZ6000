#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 已知点的坐标(x,y)，判断其所在的象限

while True:
    x = int(input("请输入x坐标："))
    y = int(input("请输入y坐标："))
    if x > 0:
        if y > 0:
            print("第一象限")
        elif y < 0:
            print("第四象限")
    elif x < 0:
        if y > 0:
            print("第二象限")
        elif y < 0:
            print("第三象限")
