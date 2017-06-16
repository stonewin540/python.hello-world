#!/usr/bin/python
# coding=utf-8
# Regular Express
# http://www.runoob.com/python/python-reg-expressions.html

import re

string = 'www.runoob.com'
print '\n---- 1 ----'
print 'Match \'www\' in \'%s\':' % string, (re.match('www', string).span())
print 'Match \'com\' in \'%s\':' % string, (re.match('com', string))

print '\n\n---- 2 ----'
line = 'Cats are smarter than dogs'
pattern = r'(.*) are (.*?) .*'
flags = re.M | re.I

matchObject = re.match(pattern, line, flags)
if matchObject:
    print 'match:', matchObject
    print 'match.group():', matchObject.group()
    print 'match.group(1):', matchObject.group(1)
    print 'match.group(2):', matchObject.group(2)

    try:
        print 'match.group(3):', matchObject.group(3)
    except IndexError, anError:
        print '\nError occurred:', anError
    else:
        pass
else:
    print 'No match'


print '\n---- 3 ----'
print 'Search \'www\' in \'%s\':' % string, re.search('www', string).span()
print 'Search \'com\' in \'%s\':' % string, re.search('com', string).span()


print '\n\n---- 4 ----'
searchObject = re.search(pattern, line, flags)
if searchObject:
    print 'search:', searchObject
    print 'search.group():', searchObject.group()
    print 'search.group(1):', searchObject.group(1)
    print 'search.group(2):', searchObject.group(2)

    try:
        print 'search.group(3):', searchObject.group(3)
    except IndexError, anError:
        print '\nError occurred:', anError
    else:
        pass
else:
    print 'Nothing found!!'


print '\n---- 5 ----'
matchObject = re.match(r'dogs', line, flags)
if matchObject:
    print 'match --> match.group()', matchObject.group()
else:
    print 'No match!'

searchObject = re.search(r'dogs', line, flags)
if searchObject:
    print 'search --> search.group()', searchObject.group()
else:
    print 'Nothing found'


print '\n---- 6 ----'
phone = '2004-959-559 # This is a foreign phone number'

replaced = re.sub(r'#.*$', '', phone)
print 'Replaced comments:', replaced

replaced = re.sub(r'\D', '', phone)
print 'Only alphanumerics:', replaced


print '\n\n---- 7 ----'


def double(matched):
    value = int(matched.group('groupName'))
    return str(value * 2)

string = 'A23G4HFD567'
print re.sub(r'(?P<groupName>\d+)', double, string)
