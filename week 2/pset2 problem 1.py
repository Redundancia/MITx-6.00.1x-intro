# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 06:40:59 2020

@author: Tuli
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def payingDebtOff(balance, annualInterestRate, monthlyPaymentRate, month = 12):
    '''
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal
    month - the number of months you want to see the debt decrease
    prints and returns the updated balance after the last month rounded to 2 decimals
    '''
    monthlyInterestRate = annualInterestRate / 12
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    if month == 1:
        print("Remaining balance: " + str(round(updatedBalance, 2)))
        return updatedBalance
    return payingDebtOff(updatedBalance, annualInterestRate, monthlyPaymentRate, month-1)

payingDebtOff(balance, annualInterestRate, monthlyPaymentRate)