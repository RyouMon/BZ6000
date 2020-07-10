#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
定义一个 Employee 雇员类，要求如下：

(1) 属性有：id、name、salary

(2) 运算符重载+：实现两个对象相加时，默认返回他们的薪水和

(3) 构造方法要求：输入 name、salary，不输入 id。id 采用自增的方式，从 1000 开始自增，第一个新增对象是 1001，第二个新增对象是 1002

(4) 根据 salary 属性，使用@property 设置属性的 get 和 set 方法。set 方法要求输入：1000-50000 范围的数
"""


class Employee:
    increment_id = 1000

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        Employee.increment_id += 1
        self.id = Employee.increment_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if 1000 <= value <= 50000:
            self._salary = value
        else:
            raise ValueError("输入的薪水超出有效范围（1000-50000）！")

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        else:
            raise TypeError("不能将Employee对象与其他类型的对象相加。")


if __name__ == '__main__':
    e1 = Employee("香菜", 5000)
    e2 = Employee("爱生", 6000)
    print("员工{name}的id为{id}，薪水为{0}。".format(e1.salary, **e1.__dict__))
    print("员工{name}的id为{id}，薪水为{0}。".format(e2.salary, **e2.__dict__))
    print("她们的工资之和为{0}。".format(e1 + e2))
