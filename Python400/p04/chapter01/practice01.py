#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
斐波那契数列（Fibonacci sequence）
"""


def fibonacci(n):
    """
    create a generator for generate fibonacci sequence of n items.
    :param n: int
    :return: generator
    :raise: ValueError if n <= 0
    """
    if n == 1:
        yield 1
    elif n == 2:
        yield 1
        yield 1
    elif n >= 3:
        last = 1
        last_last = 1
        yield 1
        yield 1
        for j in range(3, n+1):
            current = last + last_last
            yield current
            last_last = last
            last = current
    else:
        raise ValueError(f'expected: n >= 1, received: {n}')


# def fib(m):
#     def fibonacci_recursion(n):
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
#
#     for i in range(m):
#         yield fibonacci_recursion(i+1)
#
#
# fi = fib(10)
#
# for i in fi:
#     print(i, end=' ')
