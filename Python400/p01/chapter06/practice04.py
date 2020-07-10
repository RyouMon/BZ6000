#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
使用工厂模式、单例模式实现如下需求：

(1) 电脑工厂类 ComputerFactory 用于生产电脑 Computer。工厂类使用单例模式，也就是说只能有一个工厂对象。

(2) 工厂类中可以生产各种品牌的电脑：联想、华硕、神舟

(3) 各种品牌的电脑使用继承实现：

(4) 父类是 Computer 类，定义了 calculate 方法

(5) 各品牌电脑类需要重写父类的 calculate
"""


class Computer:
    def __init__(self, brand):
        self.brand = brand

    def calculate(self):
        pass


class LenovoComputer(Computer):
    def calculate(self):
        print("联想电脑正在计算...")


class AsusComputer(Computer):
    def calculate(self):
        print("华硕电脑正在计算...")


class HaseeComputer(Computer):
    def calculate(self):
        print("神州电脑正在计算...")


class ComputerFactory:
    def __new__(cls, *args, **kwargs):
        if not hasattr(ComputerFactory, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def produce(self, brand):
        if brand == "联想":
            cls = "LenovoComputer"
        elif brand == "神舟":
            cls = "HaseeComputer"
        elif brand == "华硕":
            cls = "AsusComputer"
        else:
            raise TypeError("不能生产此品牌的电脑")
        return eval(cls)(brand)


if __name__ == '__main__':
    # 测试工厂模式
    factory1 = ComputerFactory()
    lenove = factory1.produce("联想")
    asus = factory1.produce("华硕")
    hasee = factory1.produce("神舟")
    lenove.calculate()
    asus.calculate()
    hasee.calculate()
    # 测试单例模式
    factory2 = ComputerFactory()
    print(id(factory1) == id(factory2))