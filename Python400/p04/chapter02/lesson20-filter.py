#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
filter函数
"""
for i in filter(lambda x: x > 0, [1, 5, 7, -2, -1]):
    print(i, end=' ')

print('\n')

for i in filter(None, [1, 0, 7, True, False]):
    print(i, end=' ')