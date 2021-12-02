# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:38:32 2020

@author: Tuli
"""


def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
        
        
fancy_divide([0, 2, 4], 0)

def fancy_divide2(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
        
fancy_divide2([0, 2, 4], 1)


# az első az ha index 1-et használok szintén 0-át printel, szóval ha mindkettő hibát adna akkor az utolsó hibát kapjuk csak vissza