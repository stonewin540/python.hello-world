#!/usr/bin/python
# coding=utf-8

"""Client it is"""

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
print s.recv(1024)
s.close()
