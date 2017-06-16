#!/usr/bin/python
# coding=utf-8


def output(something):
    print something
    return

print '\n---- Function Definition ----'

output('Perform func')
output('It works')


def immutable(a):
    a = 10
    print a

print '\n---- 不可变对象 ----'
b = 2
immutable(b)
print b


print '\n---- 可变对象 ----'


def mutable(mylist):
    mylist.append([1, 2, 4, 3])
    print 'In func:', mylist
    return

mylist = [10, 20, 30]
mutable(mylist)
print 'Out func:', mylist

# print '\n---- 必备参数 ----'
# output() causes error throw

print '\n---- 关键字参数 ----'
output(something='My string')

print '\n---- 缺省参数 ----'


def printinfo(name, age=35):
    print 'Name:', name,
    print 'Age:', age
    return

printinfo(age=30, name='stone')
printinfo(name='stone')


print '\n---- 不定长参数 ----'


def multivar(*args):
    # def multivar(arg1, *args): the first argument is not necessary
    # print 'In func output:', arg1,
    for var in args:
        print var,
    print '\n'
    return

multivar(1)
multivar('a', 2, '\\a 0x03')
print '\a'


print '\n---- 匿名函数 ----'
add = lambda arg1, arg2: arg1 + arg2

print 'Perform:', add(1, 1)
print 'Perform:', add(10, 10)


print '\n---- return ----'


def summer(arg1, arg2):
    total = arg1 + arg2
    print 'In func:', total
    return total

total = summer(10, 20)
total = summer('a', 'b')


print '\n---- scopes ----'
print 'Can\'t modify'
total = 0


def can_not_change_global(arg1, arg2):
    total = arg1 + arg2
    print 'Inner total:', total
    return total

can_not_change_global(10, 20)
print 'Outer total:', total

print 'Modify'


def change_global(arg1, arg2):
    global total
    total = arg2 + arg1
    print 'Inner total:', total
    return
change_global(30, 40)
print 'Outer total', total
