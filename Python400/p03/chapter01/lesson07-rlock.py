#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
逻辑锁的使用，避免死锁
"""
from threading import RLock


def func01():
    lock.acquire()
    print('func1拿到锁')
    func02()
    lock.release()
    print('func1释放锁')


def func02():
    lock.acquire()
    print('func2拿到锁')
    lock.release()
    print('func2释放锁')


if __name__ == '__main__':
    lock = RLock()
    func01()
