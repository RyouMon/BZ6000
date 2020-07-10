#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用zip()函数迭代多个列表

names = ("花澤香菜", "豊崎愛生", "水瀬いのり", "佐倉綾音")
ages = (18, 19, 20, 21)
jobs = ("演员", "歌手", "偶像")


for name, age, job in zip(names, ages, jobs):
    print("{0}-{1}-{2}".format(name, age, job))