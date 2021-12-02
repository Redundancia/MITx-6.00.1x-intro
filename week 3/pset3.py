# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 03:06:21 2020

@author: Tuli
"""


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    return sorted(set(string.ascii_lowercase) ^ set(lettersGuessed))

print(sorted(getAvailableLetters(['a', 'c', 'd'])))