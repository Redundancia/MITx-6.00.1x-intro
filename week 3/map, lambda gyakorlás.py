# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def absoluteOfA(a):
    return abs(a)

# applyToEach(testList, absoluteOfA)

def addOne(a):
    return a + 1

# applyToEach(testList, addOne)

def PowerTwo(a):
    return a**2

# applyToEach(testList, PowerTwo)


# this is the same as f absoluteOfA
for elt in map(abs, testList):
    print(elt)
    
#this is the same as above
applyToEach(testList, lambda x : abs(x))
