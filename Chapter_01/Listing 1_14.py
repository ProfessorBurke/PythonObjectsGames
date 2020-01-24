"""Manage a library summer reading program."""

# Annotate and initialize variables.
max_minutes: int = -1
total_minutes: int = 0
max_name: str = None
instructions: str
num_children: int
name: str
num_minutes: int

# Display instructions to the user.
instructions = "Enter each child's name and the number of "
instructions += "minutes they read this week."
print(instructions)

# Obtain information for five children.
num_children = 0
while num_children < 5:
    name = input("What is the child's name? ")
    num_minutes = int(input("How many minutes did "
                            + name + " read this week? "))
    # Find the max so far and total.
    if num_minutes > max_minutes:
        max_minutes = num_minutes
        max_name = name
    total_minutes += num_minutes
    # Update the counter.
    num_children += 1

# Display a summary of reading information.
print(max_name + " is our star reader, with a total of " 
      + str(max_minutes) + " minutes.")
print("The total number of minutes read by all of the" 
      + " children was " + str(total_minutes) + ".")
