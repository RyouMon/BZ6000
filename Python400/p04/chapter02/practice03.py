#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
通用日志
"""

# def log(func):
#     def logged(*args, **kwargs):
#         print('logging...')
#         return func(*args, **kwargs)
#     return logged
import time


def log(func):
    def logged(*args, **kwargs):
        print('{0}: function {1} was called, args: {2}, kwargs: {3}'.format(
            time.asctime(),
            func.__qualname__,
            args,
            kwargs,
        ))
        return func(*args, **kwargs)

    return logged


@log
def func01(a, b):
    return a + b


@log
def func02(a, b, c):
    return a + b + c


print(func01(1, 2))
print(func02(1, 2, 3))
