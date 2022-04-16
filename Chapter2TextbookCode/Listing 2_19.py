"""Write reading program names to a file."""
import io

# Annotate and initialize variables.
name: str
num_minutes: int
readers_file: io.TextIOWrapper

# Display instructions to the user.
print("Enter each child's name and the number of minutes ")
print("they read this week. Enter 'quit' when done.")

# Open a file
with open("readers.txt", "w") as readers_file:
    # Obtain child information until done.
    name = input("Enter a child's name or 'quit': ")
    while name != "quit":
        num_minutes = int(input("How many minutes did "
                                + name + " read this week? "))
        # Write data to the file output stream.
        readers_file.write(name + "\n")
        readers_file.write(str(num_minutes) + "\n")
        name = input("Enter a child's name or 'quit': ")



