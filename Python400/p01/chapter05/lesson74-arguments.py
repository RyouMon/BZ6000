#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 不可变对象的传递
i = 100


def test(a):
    print("a:", id(a))
    a += 200
    print("a:", id(a))


if __name__ == '__main__':
    test(i)
