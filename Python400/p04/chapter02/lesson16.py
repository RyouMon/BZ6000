#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
functools
偏函数(partial)的使用
"""
from functools import partial


int2 = partial(int, base=2)


print(int2('10000'))
