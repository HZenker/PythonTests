#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time, threading
from concurrent import futures
from threading import Condition
import random

#global Condition not necessarry, see main
#condition = Condition()
queue = []

class Consumer(threading.Thread):
    def __init__(self,name,conditi):
        super().__init__()
        self.condition = conditi
        self.name = name
        self.ti = time.localtime()
    def run(self):
        global queue
        while True:
            self.condition.acquire()
            if not queue:
                print ("Nothing in queue, consumer is waiting")
                self.condition.wait()
                print ("Producer added something to queue and notified the consumer")
            num = queue.pop(0)
            print ("Consumed", num)
            self.condition.release()
            #time.sleep(random.random())
        

class Producer(threading.Thread):
    def __init__(self,name,conditi):
        super().__init__()
        self.condition = conditi
        self.name = name
        self.ti = time.localtime()
        self.number = 0
    def run(self):
        global queue
        while True:
            self.condition.acquire()
            self.number = self.number+1
            #print("input int: ")
            num =  self.number  #int(input())
            queue.append(num)
            print ("Produced", num)
            self.condition.notify()
            self.condition.release()
            time.sleep(random.random())
"""
if __name__ =="__main__":
    print(__name__) """
cond = Condition()

Consumer("consumer",cond).start()
Producer("himan",cond).start()


