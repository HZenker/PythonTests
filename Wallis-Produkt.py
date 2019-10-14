#! /usr/bin/env python
# -*- coding: utf-8 -*-

#import threading

import sys, time
from concurrent import futures
#from time import sleep, time

class thread1:
    pass

def piWalliProduct(n):
    pi_half = 1
    zaehler, nenner = 2.0 , 1.0 # numerator / denominator
    for i in range(n):
        pi_half  *= zaehler / nenner
        if i % 2:
            zaehler += 2
        else:
            nenner += 2
    return 2 * pi_half

print(piWalliProduct(1000000))
tt = time.time()
tlocal = time.localtime()

if __name__ =="__main__":
    N = (200000,300000,400000,5000000)
    start = time.perf_counter()
    st = sys.argv[0]
    if sys.argv.__len__() > 1:
        if sys.argv[1] == "threads":
            with futures.ThreadPoolExecutor(max_workers = 4) as ex:
                res = ex.map(piWalliProduct,N)  
    else:
        with futures.ProcessPoolExecutor(max_workers = 4) as ex:
            res = ex.map(piWalliProduct,N)
    print(list(res))
    print(time.perf_counter() - start)
    