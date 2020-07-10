#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
TCP服务器
"""
from socket import socket, AF_INET, SOCK_STREAM


# SOCK_STREAM代表TCP协议
s1 = socket(AF_INET, SOCK_STREAM)
s1.bind(('', 8080))
# 设置最大连接数
s1.listen(8)
# 进行三次握手，返回新的嵌套字对象和客户端地址
s2, addr = s1.accept()

# 使用新的嵌套字对象接收和发送信息
data = s2.recv(1024)
s2.send(b'Nice to meet you.')

# 进行四次挥手，服务端关闭
s2.close()
s1.close()