# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:28:15 2020

@author: Tuli
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    if len(aStr) == 0:
        return False
    if char == aStr[len(aStr) // 2]:
        return True
    elif char > aStr[len(aStr) // 2]:
        return isIn(char, aStr[len(aStr) // 2 + 1: len(aStr) +1])
    else:
        return isIn(char, aStr[0: len(aStr) // 2])
    
print(isIn("c", ''.join(sorted("szotyolaforduljkic"))))
