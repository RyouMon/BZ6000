#!/usr/bin/env python
# -*- coding: utf-8 -*-

for m in range(1, 10):
    for n in range(1, m+1):
        print("{0}*{1}={2}".format(m, n, m*n), end="\t")
    print()
