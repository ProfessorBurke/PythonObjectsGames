"""Read reading program names from a file."""
import io
import os.path

# Annotate and initialize variables.
data: list
readers_file: io.TextIOWrapper

# Check for the file.
if os.path.isfile("readers.txt"):
    # If the file exists, read the data in.
     with open("readers.txt", "r") as readers_file:
        data = readers_file.readlines()
else:
    # If the file does not exist, display error.
    print("The file readers.txt could not be found.")

