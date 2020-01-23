"""Manage a library summer reading program."""

# Annotate variables
num_children: int
name: str
num_minutes: int

# Obtain information for five children.
for num_children in range(5):
    name = input("What is the child's name? ")
    num_minutes = int(input("How many minutes did "
                            + name + " read this week? "))
