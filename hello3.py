#!/usr/bin/python
# coding=utf-8

import math
math.acos()

print "---- 条件语句 ----"

flag = False
name = "stone"

if name == "python":
    flag = True
    print "Welcome boss " + name
else:
    flag = False
    print "Bye boss " + name


print "\n\n---- num = 5"
num = 5
if 3 == num:
    print 'boss'
elif 2 == num:
    print 'user'
elif 1 == num:
    print 'worker'
elif num < 0:
    print 'error'
else:
    print 'roadman'


print "\n\n---- Python 竟然没有 switch 为什么呢？ ----"

print "---- num = 9"
num = 9

if 0 <= num <= 10:
    print 'hello'

print "---- num = 10"
num = 10
if num < 0 or num > 10:
    print 'hello'
else:
    print 'undefined'

print "---- num = 8"
num = 8
if (0 <= num <= 5) or (10 <= num <= 15):
    print 'hello'
else:
    print 'undefined'


print "\n\n---- 语句组 ----"
print "var = 100"
var = 100
if 100 == var: print "var is", var
