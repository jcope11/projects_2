#! /usr/bin/python3
# Guessing game - Guess a number from 1 to 100
import os
from random import randint


def play():
    number = randint(1, 100)
    guess, guesses, user_input = 0, 0, 0
    print("I'm thinking of a number from 1 to 100.")
    print("Press 'q' to quit.")
    while guess != number:
        guesses += 1
        while True:
            user_input = input("Take a guess: ")
            if user_input == 'q':
                print("Thank's for playing! Joe is awesome!!")
                exit()
            if user_input.isnumeric():
                guess = int(user_input)
                if guess > 0 and guess < 101:
                    break
                else:
                    print("Enter a number from 1 to 100.")
            else:
                print("Enter a number from 1 to 100.")
        if guess == number:
            print(f"You got it! The number was {number}.  It too you\033[91m {guesses}\033[0m guesses.")
        elif guess < number:
            print(" Higher ---->")
        else:
            print(" Lower <----")
    again = input("Would you like to play again? (y/n): ")
    if again == "y":
        play()
    else:
        print("Thanks for playing. Have a lovely day!")


play()
