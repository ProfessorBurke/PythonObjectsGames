"""Read reading program names from a file."""
import io

# Annotate and initialize variables.
data: list
readers_file: io.TextIOWrapper

# Check for the file.
try:
    # If the file exists, read the data in.
     with open("readers.txt", "r") as readers_file:
        data = readers_file.readlines()
except FileNotFoundError:
    print("The file readers.txt could not be found.")
except:
    print("Something went wrong.")

