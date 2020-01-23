"""Calculate the angle between stars in an aerial firework."""

def calc_angle(num_points: int) -> float:
    """Calculate and return the angle between points 
       evenly distributed around a circle."""
    DEGREES_CIRCLE: int = 360
    angle: float
    
    # Calculate and return the angle.
    angle = DEGREES_CIRCLE / num_points
    return angle

def main() -> None:
    """Obtain number of stars from the user, calculate
       the angle between them, and display result."""
    # Annotate variables
    num_stars: int
    angle: float
    
    # Obtain the number of stars from the user.
    num_stars = int(input("How many stars? "))

    # Calculate the angle between the stars.
    angle = calc_angle(num_stars)

    # Tell the user the angle between stars.
    print("You will need an angle of " + str(angle)
          + "\u00B0 between each star.")

main()
