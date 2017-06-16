#!/usr/bin/python
# coding=utf-8

print "---- 字符串 ----"
a = "Hello "
b = "Python"

print "%-7s" % "a + b" + ":", a + b
print "%-7s" % "a * 2" + ":", a * 2
print "%-7s" % "a[1]" + ":", a[1]
print "%-7s" % "a[1:4]" + ":", a[1:4]

print "\n----"
if "H" in a:
    print "H is in a"
else:
    print "H is not in a"

if "M" not in a:
    print "M is not in a"
else:
    print "M is in a"

print "\n---- 原始输出 ----"
print r"\n"
print R'\n'

# TODO(stone): 好吧，注释开始
print "\n---- 格式化输出 ----"
print "My name is %s and weight is %d kg!" % ('Stone', 70)
