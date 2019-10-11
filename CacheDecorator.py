#! usr/bin/env python
# -*- coding: utf-8 -*-

class CacheDecorator:
    def __init__(self):
        self.cache = {}
        self.func = None
        
    def cachedFunc(self, *args):
        if args not in self.cache:
            print("Ergebnis berechnet")
            self.cache[args] = self.func(*args)
        else:
            print("Ergebnis geladen")
        return self.cache[args]
        
    def __call__(self, func):
        self.func = func
        return self.cachedFunc

@CacheDecorator()
def fak(n):
    ergebnis = 1
    for i in range(2, n+1):
        ergebnis *= i
    return ergebnis

print(fak(10))
print(fak(20))
print(fak(20))
print(fak(10))