#!/usr/bin/python
# coding=utf-8

import os

path = '~/Desktop/'
try:
    os.chdir(path)
except BaseException, anError:
    print anError

try:
    os.chdir(path)
except OSError:
    print 'Something wrong!'

try:
    os.chdir(path)
except OSError, anError:
    print anError

try:
    os.chdir(path)
except:
    print 'Something wrong!'


print '\n\n---- ----'
try:
    os.chdir(path)
except OSError:
    print 'Error occurred'
finally:
    print 'Whatever exceptions occurred or not'

print '\n\n---- ----'
try:
    os.chdir('/Users/stone/Desktop')
except OSError:
    print 'Error occurred'
else:
    print 'Nothing goes wrong'
finally:
    print 'Whatever exceptions occurred or not'


print '\n\n---- Raise ----'


def raise_exception(arg='Fucker got it'):
    raise Exception('Just do exception', arg)

try:
    raise_exception()
# except 'Just do exception':
# TODO: 以上是教程里的写法，这样写根本就不对，无法捕获异常，下面的写法就正确了！
except Exception, e:
    print type(e)
    print 'oops', e
else:
    print 'Everything goes well!'
finally:
    print 'I don\'t know what happened?'
