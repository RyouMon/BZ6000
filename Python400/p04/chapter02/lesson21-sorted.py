#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
sorted函数
"""
for i in sorted([2, 3, 1, 4]):
    print(i, end=' ')

print('\n')

for i in sorted([2, 3, 1, 4], reverse=True):
    print(i, end=' ')

print('\n')


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{name} {age}'.format(**self.__dict__)


students = [Student('Kana', 17), Student('Aki', 18), Student('Inori', 16)]

for s in sorted(students, key=lambda x: x.age):
    print(s)
