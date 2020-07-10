#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
echo服务器
用于检测网络的连通性
"""
from socket import socket, AF_INET, SOCK_DGRAM


s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 8888))

while True:
    msg = s.recvfrom(1024)
    s.sendto(msg[0], msg[1])