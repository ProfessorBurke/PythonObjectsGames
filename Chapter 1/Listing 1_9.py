"""Validate fireworks input."""

# Annotate variables
num_stars: int
is_valid: bool

# Obtain the number of stars from the user.
num_stars = int(input("How many stars? "))

# Set the flag.
is_valid = num_stars > 0

# Message the user about input validity.
if is_valid:
    print("Your input was valid!")
else:
    print("Your input is not valid.")
