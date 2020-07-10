#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
多线程的使用
"""
from threading import Thread
from time import sleep


def func1(name):
    sleep(3)
    print("Threading:{0} start".format(name))


# 创建线程
t1 = Thread(target=func1, args=('t1',))
t2 = Thread(target=func1, args=('t2',))

# 执行线程
t1.start()
t2.start()