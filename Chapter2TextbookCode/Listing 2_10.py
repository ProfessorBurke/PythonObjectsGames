"""Manage a library summer reading program."""

# Annotate and initialize variables.
max_minutes: int = -1
total_minutes: int = 0
max_name: str = None
names: list
minutes: list
i: int = 0

# Create a list of names and minutes.
names = ["Edward", "Kamala", "Cory", "Ruth"]
minutes = [100, 200, 150, 300]

# Process the lists.
while i < len(minutes):
    # Find the max so far and total.
    if minutes[i] > max_minutes:
        max_minutes = minutes[i]
        max_name = names[i]
    total_minutes += minutes[i]
    # Update the loop control variable.
    i += 1

# Display a summary of reading information.
print(max_name + " is our star reader, with a total of " 
      + str(max_minutes) + " minutes.")
print("The total number of minutes read by all of the" 
      + " children was " + str(total_minutes) + ".")
