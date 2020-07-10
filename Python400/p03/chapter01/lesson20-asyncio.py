#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
asyncio的使用
"""
import asyncio


async def func1():
    for i in range(5):
        print('I love you!')
        await asyncio.sleep(1)


async def func2():
    for i in range(5):
        print('Sorry')
        await asyncio.sleep(1)


if __name__ == '__main__':
    g1 = func1()
    g2 = func2()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(g1, g2))