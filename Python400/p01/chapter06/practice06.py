#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
定义发动机类 Motor、底盘类 Chassis、座椅类 Seat，车辆外壳类 Shell，并使用组合
关系定义汽车类。其他要求如下：

定义汽车的 run()方法，里面需要调用 Motor 类的 work()方法，也需要调用座椅
类 Seat 的 work()方法，也需要调用底盘类 Chassis 的 work()方法。
"""


class Motor:
    def work(self):
        print("发动机启动...")


class Chassis:
    def work(self):
        print("底盘状态良好...")


class Seat:
    def work(self):
        print("请系好安全带...")


class Shell:
    pass


class Car:
    def __init__(self):
        self.shell = Shell()
        self.seat = Seat()
        self.chassis = Chassis()
        self.motor = Motor()

    def run(self):
        self.motor.work()
        self.chassis.work()
        self.seat.work()
        print('出发...')


if __name__ == '__main__':
    c = Car()
    c.run()
