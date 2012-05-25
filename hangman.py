from functions import *
from data import *

''' Driver script that runs the game ! '''
name = prompt_user_name()
print ("Hello %s - get ready to have your a-double-snake kicked " % name )

movesleft = allowedmoves
word_to_find = choose_word()
found_letters = list()

while(movesleft > 0):
    print ("\nYou have %s attempts left - just so you know " % str(movesleft))
    letter = get_letter()
    if (letter in word_to_find):
        found_letters.append(letter)
        print ("not that bad ...")
    else:
        print("HAHA - not in the word - in your face ")
        movesleft -= 1
    print("\t\t\t" + hidden_word(word_to_find,found_letters))

if (movesleft == 0):
    print("\nThe word to find was %s -- go back to elementary school" % word_to_find)
else:
    print("\nYeah well, you got it - don't be too happy about it")
    
