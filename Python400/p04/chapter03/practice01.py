#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
使用正则编写一个验证电子邮件有效性的函数
User@hostname.domain
"""
import re


def isQMail(addr):
    pattern = r'[1-9]\d{4,9}@qq.com$'
    result = re.match(pattern, addr)
    if result:
        return True
    return False


def isMail(addr):
    pattern = r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
    result = re.match(pattern, addr)
    if result:
        return True
    return False
