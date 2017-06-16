#!/usr/bin/python
# coding=utf-8

# 变量赋值
counter = 100
miles = 1000.0
name = "Stone"

print counter
print miles
print name

print "\n\n----"
# 删除对象的引用
var1 = 1
var2 = 10
print "var1: " + str(var1)
print "var2: " + str(var2)

"""
print "del var1"
del var1
# print "var1: " + str(var1) will causes crash: NameError: name 'var1' is not defined
print "var2: " + str(var2)
"""

# 字符串
print "\n\n----"
string = "Hello World!"
print string
print string[0]
print string[2:5]
print string[2]
print string * 2
print string + "TEST"

# 列表
print "\n\n----"
list = ['list', 786, 2.23, 'stone', 70.2]
tinylist = [123, 'stone']
print list
print list[0]
print list[1:3]
print list[2:]
print tinylist
print list + tinylist

# 元组
print "\n\n----"
tuple = ('tuple', 786, 2.23, 'stone', 70.2)
tinytuple = (123, 'tuple')
print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple
print tuple + tinytuple

# 字典
print '\n\n----'
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
dict["three"] = "This is three"
dict["4"] = "This is four"

tinydict = {'name': 'stone', 'code': 6734, 'dept': 'sales'}

print dict['one']
print dict[2]
print dict["three"]
print dict["4"]
print tinydict
print tinydict.keys()
print tinydict.values()
