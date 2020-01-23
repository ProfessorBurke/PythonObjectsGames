"""Calculate the angle between stars in an aerial firework."""

import random

# Annotate variables
DEGREES_CIRCLE: int = 360
num_stars: int
angle: float

# Randomly generate a number of stars.
num_stars = random.randint(2, 360)

# Calculate the angle between the stars.
angle = DEGREES_CIRCLE / num_stars

# Tell the user the angle between stars.
print("You will need an angle of " + str(angle)
      + "° between " + str(num_stars) + " stars.")
