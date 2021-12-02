# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:07:19 2020

@author: Tuli
"""

L1 = []
def recursive_practice(n):
    if n == 1:
        return n
    else:
        for i in range(n):
            L1.append(n)
            return recursive_practice(n-1)

print(recursive_practice(10))
print(L1)