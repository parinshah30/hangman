'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''

import numpy as np

#display_matrix = np.zeros(72).reshape((8,9))
display_matrix = [[" " for x in range(8)] for x in range(9)]


def init_hangman():
#    for x in np.nditer(display_matrix, op_flags=['readwrite']):
#        x[...] = 100
#        print x

    display_matrix[2][2] = '+'
    display_matrix[2][3] = '-'
    display_matrix[2][4] = '-'
    display_matrix[2][5] = '-'
    display_matrix[2][6] = '+'
    display_matrix[3][2] = '|'
    display_matrix[3][6] = '|'
    display_matrix[4][6] = '|'
    display_matrix[5][6] = '|'
    display_matrix[6][6] = '|'
    display_matrix[7][6] = '|'
    display_matrix[8][0] = '='
    display_matrix[8][1] = '='
    display_matrix[8][2] = '='
    display_matrix[8][3] = '='
    display_matrix[8][4] = '='
    display_matrix[8][5] = '='
    display_matrix[8][6] = '='
    display_matrix[8][7] = '='
#    display_matrix[2][4] = '+'
#    display_matrix[2][4] = '+'
    print display_matrix


def display_hangman():
    for x in display_matrix:
        for y in x:
            print y,
        print

word = 'cat'
missed = []
guessed = []

def init_guessed():
    for x in word:
        guessed.append("_ ")
#    guessed = list(guessed)
    print "Guessed letters: %s" % "".join(guessed)
        
def display_missed():
    print "Missed letters: ", " ".join([x for x in missed])

def display_choice():
    pass

def display_guessed():
    print "Guessed letters: %s" % "".join(guessed)

def find_input_in_word(in_char):
    for i, x in enumerate(word):
        if x == in_char:
            guessed[i] = in_char + " "


init_hangman()
init_guessed()
display_hangman()
display_missed()
display_guessed()
display_choice()

guess = 0

while guess < 6:
    in_char = raw_input("Input the next character: ")
    guess += 1
    find_input_in_word(in_char)


    display_hangman()
    display_missed()
    display_guessed()
    display_choice()

