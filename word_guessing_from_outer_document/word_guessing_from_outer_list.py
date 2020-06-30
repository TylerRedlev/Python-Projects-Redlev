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


