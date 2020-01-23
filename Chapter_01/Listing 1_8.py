"""Demonstrate the relational operators."""

# Annotate variables
value1: int
value2: int

# Obtain two values to compare from the user.
value1 = int(input("Please enter an integer: "))
value2 = int(input("Please enter another integer: "))

# Show the greater than or equal to comparison.
if value1 >= value2:
    print("The first value is greater than or equal to "
          + "the second value.")

# Show the less than or equal to comparison.
if value1 <= value2:
    print("The first value is less than or equal to "
          + "the second value.")
    
# Show the test for equality.
if value1 == value2:
    print("The values are equal.")

# Show the greater than test.
if value1 > value2:
    print("The first value is larger.")

# Show the less than test.
if value1 < value2:
    print("The first value is smaller.")
    
