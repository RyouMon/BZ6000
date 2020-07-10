#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
UDP广播
"""
from socket import socket, AF_INET, SOCK_DGRAM
from socket import SOL_SOCKET, SO_BROADCAST

dest = ('<broadcast>', 8080)
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

s.sendto(b'hello', dest)
