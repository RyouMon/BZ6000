#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用tftp下载文件
"""
from socket import socket, AF_INET, SOCK_DGRAM
import struct


s = socket(AF_INET, SOCK_DGRAM)
filename = 'test.jpg'
# 发送下载请求
download_request = struct.pack(
    '!H%dsb5sb' % len(filename), 1, filename.encode(), 0, b'octet', 0,
)
tftp_server = ('127.0.0.1', 69)
s.sendto(download_request, tftp_server)
# 开始下载文件
with open(filename, 'ab') as f:
    while True:
        # 接受数据包
        recv_data = s.recvfrom(1024)
        code, num = struct.unpack('!HH', recv_data[0][:4])
        rnd_address = recv_data[1]
        # 判断是否发生错误
        if code == '5':
            break
        # 将数据写入文件
        f.write(recv_data[0][4:])
        # 判断文件是否下载完成
        if len(recv_data[0]) < 516:
            break
        # 发送确认包
        ack = struct.pack('!HH', 4, num)
        s.sendto(ack, rnd_address)
