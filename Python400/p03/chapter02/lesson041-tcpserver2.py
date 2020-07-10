#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
使用多进程实现并发服务器
"""
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from multiprocessing import Process


def deal_with_client(socket, address):
    while True:
        data = socket.recv(1024)
        if len(data) > 0:
            print(f'received data from {address}: {data.decode()}')
        else:
            print(f'client {address} disconnected.')
            break
    socket.close()


def main():
    s1 = socket(AF_INET, SOCK_STREAM)
    s1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s1.bind(('', 8080))
    s1.listen(8)
    while True:
        print('---主进程：等待客户端连接')
        s2, address = s1.accept()
        print('---主进程：客户端连接成功')
        process = Process(target=deal_with_client, args=(s2, address))
        process.start()
        s2.close()


if __name__ == '__main__':
    main()