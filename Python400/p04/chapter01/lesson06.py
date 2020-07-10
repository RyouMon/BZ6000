#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
闭包的应用：
    在不修改原来代码的情况下添加功能
"""
import time


def log(func):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(func.__qualname__)
        f.write('\t')
        f.write(time.asctime())
        f.write('\n')


def func01():
    log(func01)
    print('call func01')


def func02():
    log(func02)
    print('call func02')


