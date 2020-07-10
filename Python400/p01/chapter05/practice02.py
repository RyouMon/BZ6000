#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 定义一个函数，将输入的参数拆成列表元素，通过sort()逆序排列后再输出。如：输入3245，输出5432


def sort(str_or_int):
    str_or_int = list(str(str_or_int))
    str_or_int.sort(reverse=True)
    return "".join(str_or_int)


print(sort(1357924680))
print(sort("acegbdf"))