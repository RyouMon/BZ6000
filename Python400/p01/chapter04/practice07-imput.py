#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 员工一共 4 人。录入这 4 位员工的薪资。全部录入后，打印提示“您已经全部录入 4名员工的薪资”。
# 最后，打印输出录入的薪资和平均薪资。

names = []
salaries = []

for i in range(4):
    name = input("请输入员工姓名：")
    salary = int(input("请输入该员工工资："))
    names.append(name)
    salaries.append(salary)

print("\n您已经全部录入4名员工的薪资:")
for name, salary in zip(names, salaries):
    print("员工{0}的工资为{1}。".format(name, salary))
print("员工的平均工资为{0}。".format(sum(salaries)/4))
