# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:37:16 2020

@author: Tuli
"""

import pylab as plt

listx=[]

listy=[]

for i in range (30):
    
    listx.append(i)
    listy.append(i*3)

plt.plot(listx,listy)

print (listx)