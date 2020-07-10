#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
reduce函数的使用
"""
from functools import reduce


li = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, li)
print(result)

result = 0
for i in li:
    result += i
print(result)