#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 可变对象的传递
l = [1, 50]


def test(a):
    print("a:", id(a))
    a.append(100)
    print("a:", id(a))


if __name__ == '__main__':
    test(l)
