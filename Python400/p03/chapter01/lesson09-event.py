#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用Event在线程间进行通信
"""
from threading import Thread, Event
from time import sleep


def bus():
    count = 0
    while True:
        if arrive.isSet():
            print("BUS: 公交已到站，请上车")
            count += 1
            sleep(0.5)
            if count % 5 == 0:
                arrive.clear()
        else:
            sleep(2)
            arrive.set()


def person():
    while True:
        if arrive.isSet():
            print("PERSON: 公交到了，快上车。")
            sleep(2)
        else:
            print("PERSON: 等公交")
            arrive.wait()


if __name__ == '__main__':
    arrive = Event()
    t1 = Thread(target=bus)
    t2 = Thread(target=person)
    t1.start()
    t2.start()
