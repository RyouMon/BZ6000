#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用yield语句切换任务
"""


def producer():
    while True:
        n = yield
        print(f'生产了第{n}个商品。')


def customer():
    p = producer()
    next(p)
    for i in range(10):
        p.send(i+1)
        print(f'消费了第{i+1}个商品。')


if __name__ == '__main__':
    customer()