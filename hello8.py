#!/usr/bin/python
# coding=utf-8

import os
import time

print '\n---- File I/O ----'

# entered = raw_input('This is raw_input, please enter something.')
# print 'Ok, you entered: %r' % entered
#
# entered = input('This is input, please enter some syntax of Python.')
# print 'Ok, you entered: %r' % entered


print '\n---- File content operations ----'
fileName = 'hello.py'
aFile = open(fileName)
print 'file name:', aFile.name
print 'file is closed:', aFile.closed
print 'file access mode:', aFile.mode
print 'file tail space:', aFile.softspace

aFile.close()
print 'Already closed'


print '\n---- Read and Write'
fileName = 'test.txt'
fileMode = 'a+'
aFile = open(fileName, fileMode)

fileContent = aFile.read()
print 'The content of the file:\n', fileContent
position = aFile.tell()
print 'Position:', position

position = aFile.seek(0, 0)
fileContent = aFile.read()
print 'Read again:\n', fileContent

aFile.write('Let\'s do some writing here.\n')

aFile.close()


# print '\n---- File operation ----'
# print 'Renaming'
# newName = 'test2.txt'
# os.rename(fileName, newName)
# time.sleep(2)
#
# print 'Removing'
# os.remove(newName)
# time.sleep(2)
#
# print '\n---- Directory Operation ----'
# directoryName = 'test'
#
# print 'Making'
# os.mkdir(directoryName)
# time.sleep(2)
#
# print 'Removing'
# os.rmdir(directoryName)
# time.sleep(2)

print 'Changing Directory'
path = os.getcwd()
print 'Current Work Directory:', path
os.chdir('/Users/stone/Desktop/')
path = os.getcwd()
print 'Current Work Directory:', path
