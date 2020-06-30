"""

1. THE TASK

Guessing a word from the list.
Write a python code in the software that may contain a couple of functions (number of functions in your program depends on yourself).
The code allows user to guess the letters of the word that is randomly chosen from the given words_list.
The words_list is located in the same folder of your python program and you need to import the list to your python code by defining a function.
A sample output is given in the following.

*---------------------------------------------
The word contains 9 letters.
Please enter one letter or a 9-letter word. A
Yes! The word contains 2 "A"s!
***A***A*
*---------------------------------------------


TO WRITE:
1) FUNCTION WHICH WILL COUNT THE LETTER COUNT IN THE WORD
2) ONE LETTER OR WORD INPUT ASKER
3) YES CONTAINS NO DOESN'T CONTAIN
4) HOW MANY TRIES COUNTER

"""

import random
# OPEN AND READ THE LINES OF THE FILE

with open('words_list.txt') as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
content = [lines.strip() for lines in content]



#CREATED A LIST FROM THE LINES OF OUR WORD FILE - THAT LIST IS CALLED "CONTENT"
#------------------------------------------------------------------------------------------



#WE CHOSE A RANDOM ELEMENT OF THE LIST AND ASSIGNED THAT ELEMENT INTO THE VARIABLE "CHOSEN"
#------------------------------------------------------------------------------------------

chosen = random.choice(content)

#WE CONVERTED THE CHOSEN STRING ELEMENT INTO A LIST

chosenList = list(chosen)

#WE WRITE THE ACTIVE STATUS OF THE NAME TO BE GUESSED AS ************

activeStatus = list(("*" * len(chosen)))

print("The word contains {} letters.".format(len(chosen)))



#WE CHOSE A RANDOM ELEMENT OF THE LIST AND ASSIGNED THAT ELEMENT INTO THE VARIABLE "CHOSEN"
#------------------------------------------------------------------------------------------

chosen = random.choice(content)

#WE CONVERTED THE CHOSEN STRING ELEMENT INTO A LIST

chosenList = list(chosen)

#WE WRITE THE ACTIVE STATUS OF THE NAME TO BE GUESSED AS ************

activeStatus = list(("*" * len(chosen)))

print("The word contains {} letters.".format(len(chosen)))



#INPUT A CHARACTER

def guess_input():

    global guess
    guess = input("Please enter one letter or a {}-letter word:".format(len(chosen)))
    guess = guess.upper()
    print(guess.upper())


#WRITING THE ITERATION FUNCTIONALITY OF THE SELECTED LIST ITEM FOR INPUTTED LETTER
#------------------------------------------------------------------------------------------

def after_guess_func():
    letter_count = int(chosenList.count(guess))
    if letter_count > 1:
        print("Yes! The word contains the {} '{}'s.".format(letter_count, guess))
    elif letter_count == 1:
        print("Yes! The word contains the letter {}".format(guess))
    else:
        print("Sorry. There are no letters '{}' in this word.".format(guess))


def guess_iteration():
    for i in range(len(chosenList)):
        if chosenList[i] == guess:
            activeStatus[i] = chosenList[i]

    print(''.join(activeStatus))