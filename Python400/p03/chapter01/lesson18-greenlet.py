#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
greenlet的使用
"""
from greenlet import greenlet


def girl(name):
    print(f'{name}: Hello!')
    g2.switch('Wen')
    print(f'{name}: How are you?')
    g2.switch('Wen')


def boy(name):
    print(f'{name}: Hey!')
    g1.switch('Kana')
    print(f'{name}: I\'m fine, thanks, and you?')


if __name__ == '__main__':
    g1 = greenlet(girl)
    g2 = greenlet(boy)
    g1.switch('Kana')