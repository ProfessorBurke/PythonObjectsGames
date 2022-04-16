"""Play a number guessing game."""

import random

# Annotate variables
number: int
guess: int

# Randomly generate a number between 1 and 50.
number = random.randint(1, 50)

# Set up the game.
print("I'm thinking of a number between 1 and 50.")

# Obtain the user's guess until they guess correctly.
guess = int(input("What is your guess? "))
while guess != number:
    if guess < number:
        print("Higher...")
    elif guess > number:
        print("Lower...")
    guess = int(input("What is your guess? "))


print("You got it!")
