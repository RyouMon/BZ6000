#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
内置函数map的使用
"""
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]


for i in map(str, list1):
    print(i, end=' ')

print('\n', '-'*10)

for j in map(pow, list1, list2):
    print(j, end=' ')