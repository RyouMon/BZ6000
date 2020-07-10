#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
简单TCP客户端
"""
from socket import socket, AF_INET, SOCK_STREAM


s1 = socket(AF_INET, SOCK_STREAM)

# 连接服务器，进行三次握手
s1.connect(('192.168.43.80', 8080))
# 向服务器发送消息
s1.send(b'hello')
# 等待服务器回复消息
msg = s1.recv(1024).decode()
print(msg)
# 关闭连接，进行四次挥手。
s1.close()