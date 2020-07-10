#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入一个毫秒数，将该数字换算成小时数，分钟数、秒数


def transform_millisecond(millisecond):
    second = millisecond/1000
    minutes = second/60
    hours = minutes/60
    return hours, minutes, second


print("{0}毫秒相当于：\n{1}小时\n{2}分钟\n{3}秒".format(4000, *transform_millisecond(4000)))