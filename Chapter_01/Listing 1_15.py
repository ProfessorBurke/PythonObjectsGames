"""Manage a library summer reading program."""

# Annotate and initialize variables.
max_minutes: int = -1
total_minutes: int = 0
max_name: str = None
name: str
num_minutes: int

# Display instructions to the user.
print("Enter each child's name and the number of minutes ")
print("they read this week. Enter 'quit' when done.")

# Obtain child information until done.
name = input("Enter a child's name or 'quit': ")
while name != "quit":
    num_minutes = int(input("How many minutes did "
                            + name + " read this week? "))
    if num_minutes > max_minutes:
        max_minutes = num_minutes
        max_name = name
    total_minutes += num_minutes
    name = input("Enter a child's name or 'quit': ")

# Display a summary of reading information.
if total_minutes != 0:
    print("The child who read the most is " + max_name 
          + ", who read " + str(max_minutes) + " minutes.")
    print("The total number of minutes read was " 
          + str(total_minutes))
