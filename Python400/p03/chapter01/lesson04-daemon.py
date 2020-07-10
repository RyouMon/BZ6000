#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
守护线程
"""
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print("Thread {0} start.".format(self.name))
        time.sleep(3)
        print("Thread {0} end.".format(self.name))


if __name__ == '__main__':
    for i in range(10):
        t = MyThread(i)
        t.setDaemon(True)
        t.start()
    print("done")
