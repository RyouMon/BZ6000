#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
进程池的基本使用
"""
from multiprocessing import Pool
from time import sleep


def func(num):
    print(f"任务{num}完成。")
    sleep(1)


if __name__ == '__main__':
    pool = Pool(5)
    for i in range(20):
        pool.apply_async(func=func, args=(i+1, ))
    pool.close()
    pool.join()
