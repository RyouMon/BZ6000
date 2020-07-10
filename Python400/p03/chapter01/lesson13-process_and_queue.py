#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
进程间的通信
"""
from multiprocessing import Process, Queue
import os


def func1(qu):
    qu.put("Message")
    print("进程{0}发送了一条消息到队列。".format(os.getpid()))


def func2(qu):
    print("进程{0}从消息队列读取了一条消息：{1}".format(os.getpid(), qu.get()))


if __name__ == '__main__':
    qu = Queue()
    p1 = Process(target=func1, args=(qu, ))
    p2 = Process(target=func2, args=(qu, ))
    p1.start()
    p2.start()