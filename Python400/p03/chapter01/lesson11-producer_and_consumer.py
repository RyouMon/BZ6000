#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
通过队列实现生产者与消费者模式
"""
from threading import Thread
from queue import Queue
from time import sleep


def producer():
    num = 1
    while True:
        if qu.qsize() < 5:
            print(f"生产了第{num}个玩具")
            qu.put(f"第{num}号玩具")
            num += 1
        sleep(1)


def consumer():
    while True:
        print("顾客购买了", qu.get())
        sleep(2)


if __name__ == '__main__':
    qu = Queue()
    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)
    t1.start()
    t2.start()