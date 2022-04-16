"""Calculate the time, height, and distance of a projectile."""

from math import sin, radians

# Annotate variables.
GRAVITY: float = 9.8
theta: float
init_velocity: float
time: float
height: float
distance: float

# Obtain initial velocity and angle from the user.
theta = float(input("What is the initial angle? "))
init_velocity = float(input("What is the intial velocity? "))
theta = radians(theta)

# Calculate the time, height, and distance.
time = (2 * init_velocity * sin(theta)) / (GRAVITY)
height = (init_velocity ** 2 * sin(theta) ** 2) / (2 * GRAVITY)

# Display the result
print("The time of flight is: " + str(time))
print("The maximum height is: " + str(height))
