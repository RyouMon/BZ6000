#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
作业3 聊天室
"""
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread, Lock
from queue import Queue

# 存放所有已连接的Socket对象
sessions = []

# 锁没有解决发生的问题
# sessions_lock = Lock()

# 存放需要发送的消息
msg = Queue()


def broadcast():
    """
    负责给所有已连接的客户端发送消息
    """
    while True:
        data = msg.get()
        # sessions_lock.acquire()
        for s in sessions:
            try:
                s.send(data)
            except ConnectionAbortedError:
                pass
        # sessions_lock.release()


def session(rnd_socket, address):
    """
    负责从一个客户端接收消息，并放入消息队列
    :param rnd_socket: 随机为客户端分配的Socket对象
    :param address: 客户端的地址
    """
    global sessions
    # sessions_lock.acquire()
    sessions.append(rnd_socket)
    # sessions_lock.release()
    while True:
        try:
            data = rnd_socket.recv(1024)
        except (ConnectionResetError, ConnectionAbortedError):
            # sessions_lock.acquire()
            sessions.remove(rnd_socket)
            # sessions_lock.release()
            msg.put(f'System: client({address[0]}:{address[1]}) left char room.'.encode('gbk'))
            break
        else:
            msg.put(f'client({address[0]}:{address[1]}): {data.decode("gbk")}'.encode('gbk'))


def main():
    """
    负责监听客户端请求，建立连接并开启一个新的对话
    """
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 8080))
    server_socket.listen(5)
    Thread(target=broadcast).start()
    while True:
        rnd_socket, address = server_socket.accept()
        msg.put(f'System: client({address[0]}:{address[1]}) entered char room.\n'.encode('gbk'))
        Thread(target=session, args=(rnd_socket, address)).start()


main()
