#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 嵌套函数


def outer():
    print("outer running...")

    def inner():
        print("inner running...")
    inner()


outer()
