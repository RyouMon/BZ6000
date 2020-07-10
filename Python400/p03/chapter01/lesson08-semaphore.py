#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
信号量的应用
"""
from threading import BoundedSemaphore, Thread
from time import sleep


def check(num):
    lock.acquire()
    sleep(3)
    print(f"第{num}个人通过了安检。")
    lock.release()


if __name__ == '__main__':
    # 控制每次通过安检的人数为3个
    lock = BoundedSemaphore(3)
    for i in range(9):
        t = Thread(target=check, args=(f'{i+1}', ))
        t.start()

