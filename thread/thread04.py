#!/usr/bin/python
# coding=utf-8

"""
Queue
"""

import Queue
import threading
import time

exitFlag = 0

threadList = ['T-1', 'T-2', 'T-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1


# Class
class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print 'Starting', self.name
        self.process_data(self.name, self.q)
        print 'Exiting', self.name

    @staticmethod
    def process_data(thread_name, q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print '%s processing %s' % (thread_name, data)
            else:
                queueLock.release()

            time.sleep(1)


# Main
for tName in threadList:
    thread = MyThread(threadID, tName, workQueue)
    thread.start()

    threads.append(thread)
    threadID += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

print 'Exiting Main Thread'
