#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
引用计数
"""
import sys


a = 12
b = a

print(sys.getrefcount(a))
