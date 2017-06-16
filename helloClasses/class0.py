#!/usr/bin/python
# coding=utf-8
# Well, test of class


class Employee:
    """Base class of all"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def display_count():
        print 'Total Employee:', Employee.empCount

    def display_employee(self):
        print 'name:', self.name, ', salary:', self.salary


class Test:
    def __init__(self):
        pass

    def prt(self):
        print self
        print self.__class__


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, id(self), self.__del__.im_func.func_name

        # members = inspect.getmembers(self, inspect.ismethod)
        # for member in members:
        #     print type(member)
        #     print member


class Parent(object):
    parentAttr = 100

    def __init__(self):
        print 'Perform parent init'

    def __repr__(self):
        return '<%s: %s>' % (str(self.__class__.__name__), str(id(self)))

    @staticmethod
    def parent_method():
        print 'Perform parent method'

    @staticmethod
    def set_attr(attr):
        Parent.parentAttr = attr

    @staticmethod
    def get_attr():
        print 'Attribute of parent:', Parent.parentAttr

    def can_be_overridden(self):
        print 'super', self.can_be_overridden.__name__


class Child(Parent):
    def __init__(self):
        # 必须与 class Parent(object): 配对出现
        super(Child, self).__init__()

        # 这种方式就无所谓了，很方便
        # Parent.__init__(self)
        print 'Perform child init'

    @staticmethod
    def child_method():
        print 'Perform child method'

    def can_be_overridden(self):
        # print 'child', inspect.getmembers(self, inspect.ismethod)
        print 'child', self.can_be_overridden.im_func


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return '<%s (%d, %d)>' % (str(self.__class__.__name__), self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


class JustCounter:
    def __init__(self):
        pass

    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
