#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
使用UDP协议接收消息
"""
from socket import socket, AF_INET, SOCK_DGRAM


s = socket(AF_INET, SOCK_DGRAM)
# AF_INET代表IPV4协议
# SOCK_DGRAM代表UDP协议                                                        

# 绑定Socket到一个地址
s.bind(('', 8888))

# 程序会在此阻塞，直到收到一条数据
msg = s.recvfrom(1024)
# 返回一个元组：(recv_data, (IP, Port))
print('rev from {0}:{1}: {2}'.format(msg[1][0], msg[1][1], msg[0].decode()))
