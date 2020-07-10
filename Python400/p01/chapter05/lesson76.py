#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 不可变对象包含可变对象


a = (10, 20, [5, 6])
print("a:", id(a))


def test01(m):
    print("m:", id(m))
    m[2][0] = 888
    print(m)
    print("m:", id(m))


if __name__ == '__main__':
    test01(a)