#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
使用线程实现消费者与生产者模式
"""
from threading import Thread
from queue import Queue
from time import sleep


def producer():
    num = 1
    while True:
        if qu.qsize() < 5:
            qu.put(num)
            print(f'生产者：生产第{num}号玩具')
            num += 1
            sleep(0.5)


def customer():
    while True:
        num = qu.get()
        print(f'消费者：购买了第{num}号玩具')
        sleep(0.5)


if __name__ == '__main__':
    qu = Queue()
    t1 = Thread(target=producer)
    t2 = Thread(target=customer)
    t1.start()
    t2.start()

