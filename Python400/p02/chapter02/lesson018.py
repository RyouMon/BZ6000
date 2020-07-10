#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("lesson016.txt", encoding="utf-8") as f:
    print("file name is {0}.".format(f.name))
    print(f.tell())
    print("text:\n{0}".format(f.read()))
    print(f.tell())
