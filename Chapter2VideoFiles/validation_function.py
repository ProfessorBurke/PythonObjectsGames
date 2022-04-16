"""Validate fireworks input."""

def valid_input(value: int, min_range: int, max_range: int) -> bool:
    """Return True if value is valid, False otherwise."""
    return value >= min_range and value <= max_range

def main():
    # Annotate variables
    num_stars: int

    # Obtain the number of stars from the user.
    num_stars = int(input("How many stars? "))

    # Check that the value is between 2 and 360.
    while not valid_input(num_stars, 2, 360):
        print("The number must be between 2 and 360.")
        num_stars = int(input("How many stars? "))

    # The input is now valid, print a message.
    print("Your input is valid.")

main()
