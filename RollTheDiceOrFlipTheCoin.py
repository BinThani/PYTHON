# Roll The Dice or Flip a coin
import random


def RollTheDice(): # Rolls the dice
    dice = random.randint(1, 6)
    print(dice)


def FlipACoin(): # Random Tails/Heads Function.
    coin = random.randint(1, 2)
    if coin == 1:
        print("Tails")
    else:
        print("Heads")


print("FlipACoin or RollTheDice")

# User Input
userInput = str(input())

# Checks UserInput
if userInput == "FlipACoin":
    print(FlipACoin())
elif userInput == "RollTheDice":
    print(RollTheDice())


# TODO Print Visual Text instead of numbers/words.
# TODO Check if user typed Dice/Flip correctly.
