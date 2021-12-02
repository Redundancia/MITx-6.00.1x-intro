# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:29:23 2020

@author: Tuli
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 02:17:30 2020

@author: Tuli
"""
s = "zyxwvutsrqponmlkjihgfedcba"

l_sub = s[0]
c_sub = s[0]
for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        c_sub += s[i]
    if s[i-1] > s[i]:
        c_sub = s[i]
    if len(c_sub) > len(l_sub):
        l_sub = c_sub
print("Longest substring in alphabetical order is: " + l_sub) 