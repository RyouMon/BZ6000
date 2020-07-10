#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入一个学生的成绩，将其转化成简单描述：不及格(小于 60)、及格(60-79)、良好(80-89)、优秀(90-100)。

while True:

    score = int(input("请输入一个分数（0-100）："))

    if 90 <= score < 100:
        print("优秀")
    elif 80 <= score < 90:
        print("良好")
    elif 60 <= score < 80:
        print("及格")
    elif 0 <= score < 60:
        print("不及格")
    else:
        print("请重新输入。")
