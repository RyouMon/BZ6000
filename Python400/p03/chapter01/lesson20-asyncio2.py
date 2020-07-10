#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
asyncio的使用
async/await语句是编写协程的推荐方式
"""
import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


asyncio.run(main())