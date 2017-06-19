#!/usr/bin/python
# coding=utf-8

print 'Content-Disposition:attachment; filename="foo.txt"'
print

fo = open('foo.txt', 'rb')

string = fo.read()
print string

fo.close()
