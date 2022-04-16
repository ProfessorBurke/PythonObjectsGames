"""Draw a random firework burst each time the user clicks."""

def calc_angle(num_points: int) -> float:
    """Calculate and return the angle between points 
       evenly distributed around a circle."""
    DEGREES_CIRCLE: int = 360
    angle: float
    
    # Calculate and return the angle.
    angle = DEGREES_CIRCLE / num_points
    return angle

def main() -> None:
    """Produce a table of stars and angles."""
    # Annotate variables
    num_stars: int
    angle: float
    
    # Print the table header.
    print("Stars\tAngle")

    # Loop over number of stars and produce table row.
    for num_stars in range(5,31,5):
        angle = calc_angle(num_stars)
        print(str(num_stars) + "\t" + str(angle))

main()
