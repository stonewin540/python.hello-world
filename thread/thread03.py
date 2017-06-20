#!/usr/bin/python
# coding=utf-8

import threading
import time


class MyThread (threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    @staticmethod
    def print_time(name, delay, counter):
        while counter:
            time.sleep(delay)
            print '%s: %s' % (name, time.ctime())
            counter -= 1

    def run(self):
        print 'Starting', self.name
        threadLock.acquire()
        self.print_time(self.name, self.counter, 5)
        threadLock.release()


threadLock = threading.Lock()
threads = []

thread1 = MyThread(1, 'T-1', 1)
thread2 = MyThread(2, 'T-2', 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print 'Exiting Main Thread'
