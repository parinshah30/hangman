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
missed = ""
def display_missed():
    print "Missed letters: ", " ".join([x for x in missed])


def display_guessed():
    pass

def display_choice():
    pass

init_hangman()
display_hangman()
display_missed()
display_guessed()
display_choice()
