from random import randint
import os, sys

# Functions

def result(points, AIpoints, Wins, Losses):
    if points > AIpoints:
        print(f"You win you had {points} points and computer had {AIpoints}")
        Wins += 1
    elif AIpoints > points:
        print(f"You lose you had {points} points and computer had {AIpoints}")
        Losses += 1
    print(f"Wins: {Wins}")
    print(f"Losses: {Losses}")

# Variables
AIpoints = 0
points = 0
totalGames = 0
Ties = 0
Wins = 0
Losses = 0
clear = lambda: os.system("cls")

# Create a list of play options

t = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer

computer = t[randint(0, 2)]

# Player
player = True
AI = False

while points != 3 or AIpoints != 3:
    if points == 3 or AIpoints == 3:
        break
    player = input("Rock, Paper, Scissors?\n")
    if player == computer:
        print("Tie")
    elif player == "Rock" and computer == "Paper":  # Rock VS Paper
        print(f"You loose\nComputer Chooses {computer}\n")
        AIpoints += 1
    elif player == "Rock" and computer == "Scissors":  # Rock VS Scissors.
        print(f"You win\nComputer Chooses {computer}\n")
        points += 1
    elif player == "Paper" and computer == "Scissors":  # Paper Vs Scissors.
        print(f"You loose\nComputer Chooses {computer}\n")
        AIpoints += 1
    elif player == "Paper" and computer == "Rock":  # Paper Vs Rock.
        print(f"You Win\nComputer Chooses {computer}\n")
        points += 1
    elif player == "Scissors" and computer == "Rock":
        print(f"You Loose\nComputer Chooses {computer}\n")
        AIpoints += 1
    elif player == "Scissors" and computer == "Paper":
        print(f"You Win\nComputer Chooses {computer}\n")
        points += 1


# Results
result(points, AIpoints, Wins, Losses)

# Restart.
restart = str(input("Do you want to play again Y/N\n"))
if restart == "y" or "Y":
    clear()
    os.system("HackerRank.py")
else:
    sys.exit("HackerRank.py")






