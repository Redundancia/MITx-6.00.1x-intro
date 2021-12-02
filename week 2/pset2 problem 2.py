# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:21:24 2020

@author: Tuli
"""

balance = 4773
annualInterestRate = 0.2


def payingDebtOffIn1Year(updatedBalance, annualInterestRate, monthlyPayment = 10, months = 12):
    '''
    updatedBalance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPayment - starts from 10, checks if it will be enough to clear debt, increments by 10 if not
    months - can change number of months, ex. if you put 24 it will check if you can clear debt in 2 years
    prints - Lowest monthly payment needed to clear debt in 1 year in increments of 10
    returns - None
    '''
    monthlyInterestRate = annualInterestRate / 12
    monthlyUnpaidBalance = updatedBalance - monthlyPayment
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    if months == 1:
        if updatedBalance <= 0:
            print("Lowest Payment: " + str(monthlyPayment))
            return
        return payingDebtOffIn1Year(balance, annualInterestRate, monthlyPayment + 10, months = 12)
    return payingDebtOffIn1Year(updatedBalance, annualInterestRate, monthlyPayment, months - 1)

payingDebtOffIn1Year(balance, annualInterestRate)