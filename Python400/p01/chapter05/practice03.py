#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 编写一个函数，计算下面的数列


def count_sequence(n):
    result = 0
    if n >= 1:
        for i in range(1, n+1):
            result += i/(i+1)
    return result


print(count_sequence(1))
print(count_sequence(2))
print(count_sequence(3))
print(count_sequence(4))