"""Validate fireworks input."""

# Annotate variables
num_stars: int

# Obtain the number of stars from the user.
num_stars = int(input("How many stars? "))

# Check that the value is between 2 and 360.
while num_stars < 2 or num_stars > 360:
    print("The number must be between 2 and 360.")
    num_stars = int(input("How many stars? "))

# The input is now valid, print a message.
print("Your input is valid.")
