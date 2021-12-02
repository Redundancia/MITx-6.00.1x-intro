# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:47:33 2020

@author: Tuli
"""

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}

argToUse = 30
print("")
print(fib_efficient(argToUse, d))