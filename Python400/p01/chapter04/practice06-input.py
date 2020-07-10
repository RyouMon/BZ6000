#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 要求输入员工的薪资，若薪资小于 0 则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资

names = []
salaries = []

while True:
    name = input("请输入员工姓名（输入q结束）：")
    if name == "q":
        print("===============")
        break
    salary = int(input("请输入该员工工资："))
    if salary < 0:
        print("输入有误请重新输入")
        continue
    else:
        names.append(name)
        salaries.append(salary)

n = len(names)  # 录入的数量
print("共录入了{0}条信息，明细如下：".format(n))
for name, salary in zip(names, salaries):
    print("员工{0}的工资为{1}。".format(name, salary))
print("员工的平均工资为{0}。".format(sum(salaries)/n))