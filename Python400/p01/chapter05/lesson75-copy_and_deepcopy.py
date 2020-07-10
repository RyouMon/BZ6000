#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 深拷贝和浅拷贝
from copy import copy, deepcopy


def test_copy():
    a = [100, 200, [300, 400]]
    b = copy(a)
    b.append(500)
    b[2].append(500)
    print(a)
    print(b)


def test_deepcopy():
    a = [100, 200, [300, 400]]
    b = deepcopy(a)
    b.append(500)
    b[2].append(500)
    print(a)
    print(b)


if __name__ == '__main__':
    test_copy()
    test_deepcopy()