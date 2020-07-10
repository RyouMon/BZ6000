#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用递归计算阶乘


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
