#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lambda表达式


def test1(a, b, c):
    return a + b + c


test2 = lambda a, b, c: a + b + c


print(test1(1, 2, 3), test2(1, 2, 3))
