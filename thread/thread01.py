#!/usr/bin/python
# coding=utf-8

import thread
import threading
import time

thread_count = 0
aLock = threading.Lock()


def increase_count():
    global aLock, thread_count
    aLock.acquire()
    thread_count += 1
    print 'increased count:', thread_count
    aLock.release()


def decrease_count():
    global aLock, thread_count
    aLock.acquire()
    thread_count -= 1
    print 'decreased count:', thread_count
    aLock.release()


def has_working_thread():
    global aLock, thread_count
    aLock.acquire()
    has = thread_count > 0
    # if thread_count > 0:
    #     has = True
    # else:
    #     has = False
    aLock.release()

    # print 'Is there some thread working:', has
    return has


def print_time(name, delay):
    """Worker for thread"""
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print '%s: %s' % (name, time.ctime())

    decrease_count()

try:
    thread.start_new_thread(print_time, ('Thread-1', 2))
    increase_count()

    thread.start_new_thread(print_time, ('Thread-2', 4))
    increase_count()
except Exception as anError:
    print '\nError occurred:', anError


# Unhandled exception in thread started by
# sys.excepthook is missing
# lost sys.stderr
# Unhandled exception in thread started by
# sys.excepthook is missing
# lost sys.stderr
while True:
    shouldBreak = not has_working_thread()
    if shouldBreak:
        print 'Well done baby, accomplished'
        break
