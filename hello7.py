#!/usr/bin/python
# coding=utf-8

import math

content = dir(math)
print 'content from \'math\':\n'

print 'Out from for loop:'
print 'globals:', globals()
print 'locals:', locals()

flag = 0
print '\n'
for string in content:
    if not flag:
        flag = 1
        print 'In for loop:'
        print 'globals:', globals()
        print 'locals:', locals()

    print string
