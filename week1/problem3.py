# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:17:30 2020

@author: Tuli
"""
s = "alzbrsgd"

l_sub = ""
c_sub = ""
for i in range(len(s)-2):
    c_sub += s[i]
    while s[i] < s[i+1]:
        c_sub += s[i+1]
        print(c_sub)
        i += 1
        print(i)
    if len(c_sub) > len(l_sub):
        l_sub = c_sub
print("Longest substring in alphabetical order is: " + l_sub) 