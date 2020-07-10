#!/usr/bin/env python
# -*-coding:utf-8-*-

# 没有使用functools.wraps装饰器的情况
# def log(func):
#     def logged(*args, **kwargs):
#         print(f'{func.__name__} is calling...')
#         return func(*args, **kwargs)
#     return logged
#
#
# @log
# def power(x):
#     """return x * x"""
#     return x * x
#
#
# power(2)
# print(power.__name__, power.__doc__)
#

# output:
# 	power is calling...
#   logged None


from functools import wraps


def log(func):
    @wraps(func)
    def logged(*args, **kwargs):
        print(f'{func.__name__} is calling...')
        return func(*args, **kwargs)
    return logged


@log
def power(x):
    """return x * x"""
    return x * x


power(2)
print(power.__name__, power.__doc__)