# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:21:24 2020

@author: Tuli
"""

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
maxMonthlyPayment = (balance * (1 + annualInterestRate / 12)**12 ) / 12
minMonthlyPayment = balance / 12

def payingDebtOff1Year(balance, annualInterestRate, maxMonthlyPayment, minMonthlyPayment, months = 12):
    '''
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    '''
    monthlyPayment = 29157.10
    currentBalance = balance
    while months >= 1:
        monthlyUnpaidBalance = currentBalance - monthlyPayment
        currentBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        months -= 1
    print(round(currentBalance, 2))
    updatedBalance = balance
    while months >= -11:
        monthlyUnpaidBalance = updatedBalance - monthlyPayment + 0.01
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        months -= 1
    print(round(updatedBalance, 2))
    if updatedBalance > 0:
        print("Lowest Payment: " + str((round(monthlyPayment, 2))))
        return


payingDebtOff1Year(balance, annualInterestRate, maxMonthlyPayment, minMonthlyPayment, months = 12)