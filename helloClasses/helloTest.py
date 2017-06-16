#!/usr/bin/python
# coding=utf-8
# Test all classes in this directory

import sys

""" 借由此次机会也展示一下 import class 和 from class import subclass 的区别
    两端代码都能正常运行，只是写起来的时候，第二种方式更方便，因为不用加 class0 了"""
# import class0
#
# t = class0.Test();
# t.prt()
#
# e = class0.Employee('stone', 1000000)
# e.display_count()
# e.display_employee()


# from class0 import Employee, Test
from class0 import *

t = Test()
t.prt()

e = Employee('stone', 1000000)
e.display_count()
e.display_employee()

print
emp1 = Employee('Zara', 2000)
emp2 = Employee('Mani', 5000)
emp1.display_employee()
emp2.display_employee()
print 'Total Employee %d' % Employee.empCount


print '\n\n---- Add iVar ----'
emp1.age = 7
print 'emp1 name:', emp1.name, ', salary:', emp1.salary, ', age:', emp1.age

print '\n---- Modify iVar ----'
emp1.age = 8
print 'emp1 name:', emp1.name, ', salary:', emp1.salary, ', age:', emp1.age

print '\n---- Try iVar on emp2 ----'
try:
    print 'emp2 name:', emp2.name, ', salary:', emp2.salary, ', age:', emp2.age
except AttributeError, anError:
    print '\nAn error occurred:', anError
else:
    print 'OK'

print '\n---- Delete iVar ----'
del emp1.age
try:
    print 'emp1 name:', emp1.name, ', salary:', emp1.salary, ', age:', emp1.age
except AttributeError, anError:
    print '\nAn error occurred:', anError
else:
    print 'OK'


print '\n\n---- Try the other way ----'
attributeName = 'age'
if not hasattr(emp2, attributeName):
    print 'emp2 does not have attributed named', attributeName
    attributeValue = 20
    print 'Let us set attribute', attributeName, 'to', attributeValue
    setattr(emp2, attributeName, 20)
    print 'emp2 name:', emp2.name, ', salary:', emp2.salary, ', age:', getattr(emp2, attributeName)
else:
    print 'emp2 has attributed named', attributeName
    print 'emp2.%s:' % attributeName, getattr(emp2, attributeName)
delattr(emp2, attributeName)


print '\n\n---- Get internal attributes ----'
print 'Employee.__doc__:', Employee.__doc__
print 'Employee.__doc__:', Employee.__name__
print 'Employee.__module__:', Employee.__module__
print 'Employee.__bases__:', Employee.__bases__
print 'Employee.__dict__:', Employee.__dict__


print '\n\n---- Reference Count ----'
pt1 = Point()
pt2 = pt1
pt3 = pt1
pt4 = Point()
print 'pt1:', id(pt1), 'ref_count:', sys.getrefcount(pt1)
print 'pt2:', id(pt2), 'ref_count:', sys.getrefcount(pt2)
print 'pt3:', id(pt3), 'ref_count:', sys.getrefcount(pt3)
print 'pt4:', id(pt4), 'ref_count:', sys.getrefcount(pt4)
del pt1
del pt2
del pt3
del pt4


print '\n\n---- Inheritance ----'
c = Child()
c.child_method()
c.parent_method()
c.set_attr(200)
c.get_attr()
c.can_be_overridden()
print c


print '\n\n---- Operator override ----'
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2


print '\n\n---- Private vs Public'
counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
try:
    print counter.__secretCount
except AttributeError as anError:
    print anError
else:
    print 'OK'
print 'Safe here'
print 'counter._JustCounter__secretCount it works'
print counter._JustCounter__secretCount
print 'but deprecated'

print 'Let us try the private method out'
try:
    counter.__this_is_private_method()
except Exception as anError:
    print 'Error occurred:', anError
else:
    print 'OK'

print 'Just list private variable, counter._JustCounter__this_is_private_method()'
counter._JustCounter__this_is_private_method()


print '\n\nSubJustCounter init'
counter = SubJustCounter()
counter.count()
counter.count()
print 'counter.publicCount:', counter.publicCount
print 'counter._JustCounter__secretCount:', counter._JustCounter__secretCount
counter.show_the_protected()
print 'practise'
