# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:05:43 2020

@author: Tuli
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    return max([len(aDict[keys]) for keys in aDict])

print(biggest(animals))


def biggest(aDict):
    
    return max((len(aDict[k]), k) for k in aDict)[1]

print(biggest(animals))

def biggest(aDict):
    
    return max((len(aDict[k]), k) for k in aDict)[1]

print(biggest(animals))