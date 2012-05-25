'''contains the actions used for the game '''

#!/usr/bin/python2.7

from data import *
from random import randrange

def prompt_user_name():
    '''Prompts the user for name. Returns the name entered by the user'''
    name_entered = raw_input("What's your name ? :) ")
    name_entered = name_entered.capitalize()
    if not name_entered.isalpha() or len(name_entered)<3:
        print("Your name is kinda messed up... I don't like it. Try again.")
        return prompt_user_name()
    else:
        return name_entered

def get_letter():
    letter = raw_input("Give me a letter now : ")
    letter = letter.lower()
    if not letter.isalpha() or len(letter)>1 :
        print("Who do you think you're kidding? This is not a LETTER ! Try again...")
        return get_letter()
    else:
        return letter

def choose_word():
    index = randrange(len(wordlist))
    return wordlist[index]

def hidden_word(word, found_letters):
    mystery = ""
    for letter in word:
        if letter in found_letters:
            mystery += letter
        else:
            mystery += '*'
    return mystery
    
    
    

if __name__ == '__main__':
    word = choose_word()
    print word

