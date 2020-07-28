# Better version than the last one.

# Modules
import random

# Variables
AInumber = random.randint(1, 20)
Tries = 6
number = 0
AIpoints = 0
userpoints = 0

# Checks for userInput.
while True:
    print("Guess a number between 0 - 20")
    if number < 1 or number > 20:
        print("Cannot include numbers less than 0/Greater than 20")
    else:
        break
    while Tries > 0:
        try:
            number = int(input())
        except ValueError:
            print("Sorry I didn't Understand that")
        if number == AInumber:
            print(f"You Guessed {number}!\n AI Guessed {AInumber}!")
            break
        elif number < AInumber:
            print("higher")
            Tries -= 1
        elif number > AInumber:
            print("Lower")
            Tries -= 1

