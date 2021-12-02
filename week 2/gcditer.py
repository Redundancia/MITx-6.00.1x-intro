# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:57:45 2020

@author: Tuli
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    for i in range( min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            break
    return i

gcdIter(60,6)