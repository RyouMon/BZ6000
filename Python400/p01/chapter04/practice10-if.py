#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入一个分数。分数在 0-100 之间。90 以上是 A,80 以上是 B，70 以上是 C，60 以上是 D。60 以下是 E。

while True:

    score = int(input("请输入一个分数（0-100）："))

    if 90 <= score < 100:
        print("A")
    elif 80 <= score < 90:
        print("B")
    elif 70 <= score < 80:
        print("C")
    elif 60 <= score < 70:
        print("D")
    elif 0 <= score < 60:
        print("E")
    else:
        print("请重新输入。")
