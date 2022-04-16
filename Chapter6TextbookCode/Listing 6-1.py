"""Write and read a list of integers using the pickle library."""

import pickle
import io

def main():
    """Demonstrate the pickle library."""
    # Annotate variables
    file_out: io.BufferedWriter
    file_in: io.BufferedReader
    numbers_out: list = [1, 2, 3, 4, 5]
    numbers_in: list

    # Write the list to a binary file.
    print("List before pickling: " + str(numbers_out))
    with open("pickle_test", "wb") as file_out:
        pickle.dump(numbers_out, file_out)

    # Read a list from a binary file.
    with open("pickle_test", "rb") as file_in:
        numbers_in = pickle.load(file_in)
    print("List after unpickling: " + str(numbers_in))

main()

    
