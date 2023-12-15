"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    guess word and play Hangman game
    """
    answer = random_word()  # get a random word
    guessed_letter = set()  # an empty set to store guessed letters.
    N_TURNS = 7
    dashed_word = ""  # the word with dashes.
    print("The world looks like:" + word(answer, guessed_letter))
    print("You have " + str(N_TURNS) + " wrong guesses left")

    while N_TURNS > 0:
        input_ch = input("Your guess:").lower()  # convert guessed numbers to lowercase.
        if not valid_input(input_ch): # check if the input is in correct format
            print("illegal format.")
            continue

        guessed_letter.add(input_ch)  # Add the guessed character to the set
        if input_ch not in answer.lower():
            N_TURNS -= 1 # decrease the number of remaining guesses.
            print("There is no " + input_ch + "'s" + " in the world")
            print("You have " + str(N_TURNS) + " wrong guesses left")
        else:
            dashed_word = word(answer, guessed_letter)
            print("You are correct.")
            print("The word looks like:" + dashed_word)

        if dashed_word == answer:
            print("You win")
            break

    if N_TURNS == 0: # the number of remaining guesses is 0
        print("You are completely hung")
        print("The answer is: " + answer)


def word(answer, guessed_letter):
    """
    param answer: the correct answer from random_word( )
    param guessed_letter : record the letters guessed
    return : the word with dashes, showing the accurate guessed words
    """
    result = ""
    for ch in answer:
        if ch.lower() in guessed_letter:
            result += ch
        else:
            result += "-"
    return result


def valid_input(input_ch):  # check if the input is a valid single alphabetical character.
    return input_ch.isalpha() and len(input_ch) == 1


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
