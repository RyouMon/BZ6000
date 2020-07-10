#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
打印目录结构
"""
import os


def get_all_files(path, level=1):
    child_files = os.listdir(path)
    for file in child_files:
        filepath = os.path.join(path, file)
        print("-"*level, filepath)
        if os.path.isdir(filepath):
            get_all_files(filepath, level+1)


get_all_files(r"E:\Live")