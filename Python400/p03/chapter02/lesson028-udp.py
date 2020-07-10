#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
使用UDP协议发送消息
"""
from socket import socket, AF_INET, SOCK_DGRAM


s = socket(AF_INET, SOCK_DGRAM)
# AF_INET代表IPV4协议
# SOCK_DGRAM代表UDP协议

s.sendto('hello'.encode(), ('169.254.210.86', 1024))
