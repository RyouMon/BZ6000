#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
利用队列进行线程间的通信，队列自带锁，可以保证线程的安全
"""
from queue import Queue


qu = Queue()

qu.put(1)
qu.put(2)
qu.put(3)

print(qu.get())
print(qu.get())
print(qu.get())
