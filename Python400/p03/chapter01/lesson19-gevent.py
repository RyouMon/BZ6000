#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gevent的使用
"""
import gevent
from gevent import monkey
monkey.patch_all()
from time import sleep


def girl(name):
    print(f'{name}: Hello!')
    sleep(1)
    print(f'{name}: How are you?')


def boy(name):
    print(f'{name}: Hey!')
    sleep(1)
    print(f'{name}: I\'m fine, thanks, and you?')


if __name__ == '__main__':
    g1 = gevent.spawn(girl, 'Kana')
    g2 = gevent.spawn(boy, 'Wen')
    g1.join()
    g2.join()
