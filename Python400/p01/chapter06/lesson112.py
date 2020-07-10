#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
对象的深复制与浅复制
"""
import copy


class People:
    def __init__(self, name):
        self.name = name


class Family:
    def __init__(self, mother, father, *children):
        self.mother = mother
        self.father = father
        self.children = list(children)


class Mother(People):
    pass


class Father(People):
    pass


class Child(People):
    pass


f1 = Family(
    Mother("Lily"), Father("John"), Child("Joe"), Child("Lisa")
)
f2 = copy.copy(f1)
f3 = copy.deepcopy(f1)

print(f1, f1.mother, f1.father, f1.children)
print(f2, f2.mother, f2.father, f2.children)
print(f3, f3.mother, f3.father, f3.children)



