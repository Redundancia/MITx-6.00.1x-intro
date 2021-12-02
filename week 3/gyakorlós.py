# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 01:07:17 2020

@author: Tuli
"""
    
fork = "abcedaa"
list1 = ['a', 'b', 'c', 'e']
   

     
result = all([False for i in fork if i not in list1])
print(result)



print(set(fork) ^ set(list1))