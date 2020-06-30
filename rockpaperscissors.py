from random import randint

# list of play options
play = ["Rock", "Paper", "Scissors"]

# get the user input
player = input("Rock, Paper, Scissors? ")

# get the user input
computer = play[randint(0, 2)]
print('computer: {}'.format(computer))