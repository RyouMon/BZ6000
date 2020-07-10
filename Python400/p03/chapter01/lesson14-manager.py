#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用Manager在进程间共享数据
"""
from multiprocessing import Process, Manager, current_process


def func1(_list, data):
    _list.append(data)
    print("进程{0}，向管理器托管了一条数据：{1}".format(current_process().pid, data))


def func2(_list):
    print("进程{0}, 向管理器取出了一条数据: {1}".format(current_process().pid, _list.pop()))


if __name__ == '__main__':
    with Manager() as mgr:
        m_list = mgr.list()
        p1 = Process(target=func1, args=(m_list, 3.1415926))
        p2 = Process(target=func2, args=(m_list, ))
        p1.start()
        p1.join()
        p2.start()
        p2.join()