#!/usr/bin/env python
# -*-coding:utf-8-*-
from threading import Thread, Lock
from time import sleep


def func01():
    lock1.acquire()
    print("厨师1拿到菜刀-切菜")
    sleep(2)
    lock2.acquire()
    print("厨师1拿到锅-下锅")
    lock1.release()
    print("厨师1切完菜-还刀")
    lock2.release()
    print("厨师1做完菜-还锅")


def func02():
    lock2.acquire()
    print("厨师2拿到锅-热锅")
    lock1.acquire()
    print("厨师2拿到菜刀-切菜")
    lock1.release()
    print("厨师1切完菜-还刀")
    lock2.release()
    print("厨师1做完菜-还锅")


if __name__ == '__main__':
    # 假如两个厨师公用一把菜刀和一口锅
    lock1 = Lock()  # 菜刀
    lock2 = Lock()  # 锅
    t1 = Thread(target=func01)  # 厨师1
    t2 = Thread(target=func02)  # 厨师2
    t1.start()
    t2.start()
