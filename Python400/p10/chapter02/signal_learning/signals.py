#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pre_save_receive(sender, **kwargs):
    print(f'模型保存之前：{sender}, kwargs: {kwargs}')
