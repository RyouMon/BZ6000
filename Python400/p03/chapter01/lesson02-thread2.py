#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print("Thread {0}...".format(self.name))
        sleep(3)


if __name__ == '__main__':
    t1 = MyThread("1")
    t2 = MyThread("2")
    t1.start()
    t2.start()