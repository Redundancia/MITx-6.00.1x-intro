# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True

    #set:
    return set(secretWord) <= set(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ""
    for l in secretWord:
        if l in lettersGuessed:
            guessed_word += l
        else:
            guessed_word += "_ "
    return guessed_word

    #oneliner:
    return "".join(l if l in lettersGuessed else "_ " for l in secretWord)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    available_letters = ""
    
    for l in string.ascii_lowercase:
        if l not in lettersGuessed:
            available_letters += l
    return available_letters

    #oneliner:
    return "".join(c for c in "abcdefghijklmnopqrstuvwxyz" if c not in [lettersGuessed])
    
    #set:
    return "".join(sorted(set("abcdefghijklmnopqrstuvwxyz") - set(lettersGuessed)))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {0} letters long".format(len(secretWord)))
    
    lives = 8
    lettersGuessed = []
    
    guessLetter(lives, lettersGuessed, secretWord)


def guessLetter(lives, lettersGuessed, secretWord):
    availableLetters = getAvailableLetters(lettersGuessed)

    print("------------")
    if lives == 0:
        print("Sorry you ran out of guesses. The word was {}.".format(secretWord))
        return
    
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
        return
    
    print("You have {0} guesses left.".format(lives))
    print("Available letters: {}".format(availableLetters))
    guess = input("Please guess a letter: ")
    
    if guess.lower() in lettersGuessed:
        print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        return guessLetter(lives, lettersGuessed, secretWord)
    
    if guess.lower() in availableLetters:
        lettersGuessed += guess.lower()
        if guess.lower() not in secretWord:
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            return guessLetter(lives - 1, lettersGuessed, secretWord)
        print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        return guessLetter(lives, lettersGuessed, secretWord)
    return guessLetter(lives, lettersGuessed, secretWord)



secretWord = "sea"
#secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
