# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:43:55 2020

@author: Tuli
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    how_Many = 0
    for keys in aDict.keys():
        how_Many += len(aDict[keys])
    return how_Many

print(how_many(animals))


#list comprehension practice
list1 = [i for i in range(15) if i % 2 == 0]
print(list1)

list1 = []
for i in range(15):
    if i % 2 == 0:
        list1 += [i]
print(list1)


