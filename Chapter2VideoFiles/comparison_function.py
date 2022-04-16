"""Compare two numeric values obtained from the user."""

def compare(val1: int, val2: int) -> int:
    """Return a positive int if val1>val2, a negative
       int if val2>val1, and 0 otherwise."""
    return val1 - val2

def main() -> None:
    # Annotate variables
    num1: int
    num2: int
    comparison: int

    # Obtain values from the user.
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    # Compare and report the result.
    comparison = compare(num1, num2)
    if comparison > 0:
        print("The first number is larger.")
    elif comparison < 0:
        print("The second number is larger.")
    else:
        print("The numbers are equal.")

main()
