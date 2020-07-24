# Number Guessing Game.

# Modules
import random
import os
import sys

# Variables
i = 0
clear = lambda: os.system("cls")

# Computer will choose Random number 0 < n < 20.
computer = random.randint(0, 20)

print("Im thinking of a number between 0 and 20...")

# Checks Input and comapares with the AI.
while i <= 5:
    i += 1
    userInput = int(input())
    print(f"Chances: {6 - i}")
    if userInput < computer:
        print(f"Greater than {userInput}")
    elif userInput > computer:
        print(f"Less than {userInput}")
    else:
        print(f"Correct Computer is {computer} and you choose {userInput}")
        break

# Restart
choice = str(input("Would you like to play again (y/n)\n"))
if choice == "y" or "Y":
    clear()
    os.system("GuessGame.py")




# TODO Restart game if user wanted. still not fixed ...
