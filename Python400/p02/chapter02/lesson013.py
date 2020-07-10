#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    f = open("test.txt", "a")
    f.write("test")
except Exception as e:
    print(e)
finally:
    f.close()


with open("test.txt", "a") as f:
    f.write("test")
