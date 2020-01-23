"""Validate fireworks input."""

def in_range(value: int) -> bool:
    """Return True if value is between 2 and 360 inclusive."""
    result: bool = False
    if value >= 2 and value <= 360:
        result = True
    return result

def main() -> None:
    """Obtain and validate number of stars."""
    # Annotate variable
    num_stars: int
    
    # Obtain the number of stars from the user.
    num_stars = int(input("How many stars? "))

    # Check that the value is between 2 and 360.
    while not in_range(num_stars):
        print("The number must be between 2 and 360.")
        num_stars = int(input("How many stars? "))

    # The input is now valid, print a message.
    print("Your input is valid.")

main()
