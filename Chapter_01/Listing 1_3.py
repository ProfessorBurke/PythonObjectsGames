"""Demonstrate common mathematical equations
   using the math library."""

import math

# Declare some constants using the math library.
PI_OVER_6: float = math.radians(30)
PI_OVER_3: float = math.pi / 3
RADIUS: int = 100

# Annotate variables
x: float
y: float
distance: float
y_floor: int
y_ceil: int
y_round: int

# Compute the x and y coordinates of a star.
x = RADIUS * math.cos(PI_OVER_6)
y = RADIUS * math.sin(PI_OVER_6)

# Compute the distance from origin to the star.
distance = math.sqrt(pow(x,2) + pow(y,2))

# Find the integers above and below the y coordinate.
y_floor = math.floor(y)
y_ceil = math.ceil(y)
y_round = round(y)

# Print the computed values.
print("x = " + str(x) + "\ny = " + str(y)
      + "\ndistance = " + str(distance)
      + "\ny floored = " + str(y_floor)
      + "\ny ceilinged = " + str(y_ceil)
      + "\ny rounded = " + str(y_round))
