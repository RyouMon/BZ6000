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
    print('call func01')


def func02():
    print('call func02')


def log_func(func):
    def func_in():
        log(func)
        func()
    return func_in


func01 = log_func(func01)
func02 = log_func(func02)


