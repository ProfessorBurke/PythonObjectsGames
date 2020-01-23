"""Read reading program names from a file."""
import io

# Annotate and initialize variables.
name: str
minutes: int
minutes_str: str
readers_file: io.TextIOWrapper

# Open a file
with open("readers.txt", "r") as readers_file:
    # Read child information from the file until the end.
    name = readers_file.readline()
    while name != "":
        name = name.strip()
        minutes_str = readers_file.readline()
        minutes = int(minutes_str)
        
        # Display the values to the user
        print("{} read {} minutes.".format(name, minutes))

        # Read the next name or eof
        name = readers_file.readline()


