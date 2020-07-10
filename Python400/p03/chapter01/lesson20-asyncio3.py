#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
asyncio的使用
async/await语句编写协程的推荐方式
"""
import asyncio
import time


def test01():
    async def say_after(delay, what):
        await asyncio.sleep(delay)
        print(what)

    async def main():
        print(f'started at {time.strftime("%X")}')

        await say_after(1, 'hello')
        await say_after(2, 'world')

        print(f'finished at {time.strftime("%X")}')

    asyncio.run(main())


def test02():
    async def say_after(delay, what):
        await asyncio.sleep(delay)
        print(what)

    async def main():
        task1 = asyncio.create_task(say_after(1, 'hello'))
        task2 = asyncio.create_task(say_after(2, 'world'))

        print(f'started at {time.strftime("%X")}')

        await task1
        await task2

        print(f'finished at {time.strftime("%X")}')

    asyncio.run(main())


if __name__ == '__main__':
    test01()
    test02()
