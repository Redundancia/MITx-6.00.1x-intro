# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:10:48 2020

@author: Tuli
"""

def genFib():
    fib_1 = 1
    fib_2 = 0
    while True:
        next = fib_1 + fib_2
        yield next
        fib_2 = fib_1
        fib_1 = next
        
foo = genFib()

# you use with foo.__next__(), but if you run this you will only get 1 every tiem because it will run the funciton from start as well
# so you have to run foo.__next__() in the command line