# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 07:02:58 2020

@author: Tuli
"""

import timeit
time = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(time)