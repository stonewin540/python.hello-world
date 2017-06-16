#!/usr/bin/python
# coding=utf-8

import time
import calendar

print "---- Start Time ----"
ticks = time.time()
print "Current time:", ticks

print "\n---- Time tuple ----"
print "Nil parameters"
localtime = time.localtime()
print "Current time:", localtime

print "time() parameter"
localtime = time.localtime(ticks)
print "Current time:", localtime

print "\n---- Formatted time ----"
print "Nil"
localtime = time.asctime()
print "Current time:", localtime

print "Non-null"
localtime = time.asctime(time.localtime(time.time()))
print "Current time:", localtime

print "\n---- Formatted date ----"
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
datetime = 'Thu 15 Jun 10:54:19 2017'
print time.mktime(time.strptime(datetime, '%a %d %b %H:%M:%S %Y'))

print "\n---- End Time ----"

print "\n---- Start Date ----\n"

cal = calendar.month(2017, 6)
print 'Calendar of 2017.6'
print cal

print 'calendar()'
print '', calendar.calendar(2017)

print "\n---- End date ----"
