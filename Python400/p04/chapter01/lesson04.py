#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
闭包的使用
"""

# 问题1 求两个数字之和
# 传统方法：


def sum_a_b(a, b):
    return a + b


def sum_a_b_out(a):
    def sum_a_b_in(b):
        return a + b
    return sum_a_b_in

