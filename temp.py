# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:21:32 2020

@author: Tuli
"""

list1 = ["1", "2", "3", "From", "4", "5"]
for i in list1:
    if i.startswith("From") : continue
    print(i)


class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self,other):
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else: return False
        
    def __repr__(self):
        # this formatting doesnt work on edx site
        return f"Coordinate({self.getX()},{self.getY()})"
    
x = Coordinate(3,4)
y = Coordinate(4,3)

print(x == y)