"""Calculate the angle between stars in an aerial firework."""

# Annotate variables.
DEGREES_CIRCLE: int = 360
num_stars: int
angle: float

# Obtain the number of stars from the user.
num_stars = int(input("How many stars? "))

# Calculate the angle between the stars if greater than zero.
if num_stars > 0:
    angle = DEGREES_CIRCLE / num_stars

    # Tell the user the angle between the stars.
    print("You will need an angle of " + str(angle) + " degrees between "
          + str(num_stars) + " stars.")
else:
    print("The number of stars must be a positive integer.")
