#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
进程池上下文管理器的使用方法。
进程池map方法的使用。
"""
from multiprocessing import Pool
from time import sleep


def func(num):
    print(f"任务{num}完成。")
    sleep(1)
    return pow(num, 2)


if __name__ == '__main__':
    with Pool(5) as pool:
        results = pool.map(func=func, iterable=[i+1 for i in range(10)])
        print(results)
