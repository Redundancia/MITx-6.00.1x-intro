# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 02:23:32 2020

@author: Tuli
"""

secretWord = "myass"
lettersGuessed = ['a', 'b', 'c', 's']
tip = ""
for c in secretWord:
    if c in lettersGuessed:
        tip += c + " " 
    else:
        tip += "_ "
# return tip
        
print(tip)

y = [i for i in secretWord if i in lettersGuessed]
x = " ".join([i if i in lettersGuessed else "_" for i in secretWord])
print(x)