"""Load an image file based on user input."""

# Import and initialize pygame
import pygame
pygame.init()

# Annotate variables
color: str
star: pygame.Surface 

# Ask the user what color star they want.
print("Stars can be red, blue, green, or yellow.")
color = input("What color would you like? ")

# Load the appropriate image.
if color == "red":
    star = pygame.image.load("red_star.png")
elif color == "blue":
    star = pygame.image.load("blue_star.png")
elif color == "green":
    star = pygame.image.load("green_star.png")
else:
    star = pygame.image.load("yellow_star.png")

# Quit when the user presses enter.
input("Press enter to quit...")
pygame.quit()
