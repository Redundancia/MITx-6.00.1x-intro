# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:17:32 2020

@author: Tuli
"""

def genPrimes():
    primes = []
    prime = 2
    while True:
        if all([False for i in range(len(primes)) if prime % primes[i] == 0]):
            yield prime
            primes.append(prime)
            
        prime += 1
        
foooo = genPrimes()


def genPrimes():
    last_number = 1
    while True:
        next = last_number + 1
        is_next_a_prime = True
        for i in range(2, next):
            if next % i == 0:
                is_next_a_prime = False
                break
        if is_next_a_prime == True:
            yield next
        last_number += 1
        
        
fooo = genPrimes()

# you use with fooo.__next__(), but if you run this you will only get 1 every tiem because it will run the funciton from start as well
# so you have to run fooo.__next__() in the command line