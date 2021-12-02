# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:28:19 2020

@author: Tuli
"""

guess = 50
min_num = 0
max_num = 100
print("Please think of a number between 0 and 100!")
while True:
    print("Is your secret number " + str(guess) + "?")
    indicator = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if indicator == "h":
        max_num = guess
        guess = (guess + min_num) // 2
    elif indicator == "l":
        min_num = guess
        guess = (guess + max_num) // 2
    elif indicator == "c":
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
        