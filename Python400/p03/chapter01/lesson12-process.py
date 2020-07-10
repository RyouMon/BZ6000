#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
进程的基本使用
"""
from multiprocessing import Process
from time import sleep
import os


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print('当前进程号：{0}'.format(os.getpid()))
        print('父进程号：{0}'.format(os.getppid()))
        print("开始执行进程{0}".format(self.name))
        sleep(2)
        print("结束执行进程{0}".format(self.name))


if __name__ == '__main__':
    print('当前进程号：{0}'.format(os.getpid()))
    p1 = MyProcess('p1')
    p2 = MyProcess('p2')
    p1.start()
    p2.start()