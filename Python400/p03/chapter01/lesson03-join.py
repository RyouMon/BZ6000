#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
线程对象的Join方法
"""
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print("Thread {0}...".format(self.name))
        time.sleep(3)


if __name__ == '__main__':
    start = time.time()
    t1 = MyThread("1")
    t2 = MyThread("2")
    t1.start()
    t2.start()
    # 主线程会等待子线程结束后才继续执行
    t1.join()
    t2.join()
    end = time.time()
    print("run in {0}s.".format(end-start))