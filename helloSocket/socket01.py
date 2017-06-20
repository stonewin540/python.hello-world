#!/usr/bin/python
# coding=utf-8

"""
Server it is
"""

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

try:
    while True:
        # c, address = s.accept()
        # print address
        # c.send('Welcome home buddy!')
        # c.close()
        ret = s.accept()
        c = ret[0]
        address = ret[1]
        print address
        c.send('Welcome home buddy!')
        c.close()
except Exception, anError:
    print anError

print 'All done'
