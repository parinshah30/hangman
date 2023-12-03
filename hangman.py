# ascii

'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
import os
import random

# assets
wrong_guess = 0
display_matrix = [[" " for x in range(8)] for x in range(9)]
def init_hangman():
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


def display_hangman():
    for x in display_matrix:
        print "".join(x)

word = random.choice(['cat', 'elephant', 'lion'])
missed = []
guessed = []
# logic
def check_answer():
    return word == "".join(guessed)

def init_guessed():
    for x in word:
        guessed.append("_")

def display_missed():
    print "Missed letters: ", " ".join([x for x in missed])

def display_guessed():
    print "Guessed letters: %s" % " ".join(guessed)

def find_input_in_word(in_char):
    global wrong_guess
    find = 0
    if guessed.count(in_char) or missed.count(in_char):
        print "Character already tried. Try something else"
        return 0
    for i, x in enumerate(word):
        if x == in_char:
            guessed[i] = in_char
            find = 1

    if not find:
        missed.append(in_char)
        wrong_guess += 1
        edit_hangman()

    return find

def edit_hangman():
    if wrong_guess == 1:
        display_matrix[4][2] = 'O'
    elif wrong_guess == 2:
        display_matrix[5][2] = '|'
    elif wrong_guess == 3:
        display_matrix[5][1] = '/'
    elif wrong_guess == 4:
        display_matrix[5][3] = '\\'
    elif wrong_guess == 5:
        display_matrix[6][1] = '/'
    elif wrong_guess == 6:
        display_matrix[6][3] = '\\'

# banner

def banner():
    print " -- H A N G M A N --"

os.system("clear")
banner()
init_hangman()
init_guessed()
display_hangman()
display_missed()
display_guessed()


while wrong_guess < 6:
    in_char = raw_input("Input the next character: ")
    if in_char.strip() and in_char.isalpha():
        right_guess = find_input_in_word(in_char)

    os.system("clear")
    banner()
    display_hangman()
    display_missed()
    display_guessed()
    if check_answer():
        print "YOU WIN!!!"
        break

