#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
如下代码，使用图文分析整个内存过程：

1、Student类的定义，
Python开辟了一片空间用来储存Student所有的属性，
并将Student指向这片空间，
空间中所有的属性分别将指针指向它们的定义。
2、Student的实例化，
Python开辟出一片空间用来储存实例的所有属性，并将s1指向这片空间，
对象s1中所有从属于类的属性全部指向现有的定义；
对象隐式调用__init__()方法进行初始化，
向对象的定义中添加实例属性name和score并将它们指向给定的值，
同时将类属性count的值加1。
"""


class Student:
    company = "尚学堂"  # 类属性
    count = 0  # 类属性

    def __init__(self, name, score):
        self.name = name  # 实例属性
        self.score = score
        Student.count = Student.count + 1

    def say_score(self):  # 实例方法
        print("我的公司是：", Student.company)
        print(self.name, '的分数是：', self.score)


s1 = Student('高淇', 80)  # s1 是实例对象，自动调用__init__()方法
s1.say_score()
print('一共创建{0}个 Student 对象'.format(Student.count))
