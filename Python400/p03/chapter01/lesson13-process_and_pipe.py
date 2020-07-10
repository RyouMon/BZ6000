#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
进程间的通信，使用管道（Pipe）
"""
from multiprocessing import Process, Pipe, current_process


def func1(pipe, message):
    pipe.send(message)
    print("进程{0}向管道一条消息，消息内容：{1}".format(current_process().pid, message))


def func2(pipe):
    print("进程{0}从管道接受了一条消息：{1}".format(current_process().pid, pipe.recv()))


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    p1 = Process(target=func1, args=(conn1, "Hello!"))
    p2 = Process(target=func2, args=(conn2, ))
    p1.start()
    p2.start()
