"""Manage a library summer reading program."""

from Reader import *

# Define menu constants
ADD: int = 1
VIEW_ALL: int = 2
QUIT: int = 3
MENU_TEXT: str = ("1. Add a reader\n2. View all readers" +
                  "\n3. Quit")

def menu() -> int:
    """Obtain and return the user's menu choice."""
    choice: int = 0
    while choice < ADD or choice > QUIT:
        print(MENU_TEXT)
        choice = int(input("Please enter the number of "
                           + "your choice: "))
    return choice
    
def main() -> None:
    """Manage a list of Reader objects."""
    # Annotate and initialize variables.
    readers: list = []
    choice: int = 0
    name: str
    has_minutes: str
    minutes: int
    reader: Reader
    
    # Greet the user.
    print("Welcome!  How can I help you manage the "
          + "reading program?")    

    # Process a menu choice.
    while choice != QUIT:
        choice = menu()
        if choice == ADD:
            # Create and add a reader to the list.
            name = input("What is the child's name? ")
            has_minutes = input("Has the child read? (Y or N) ")
            if has_minutes == "Y":
                minutes = int(input("How many minutes? "))
                reader = Reader(name, minutes)
            else:
                reader = Reader(name)
            readers.append(reader)
        elif choice == VIEW_ALL:
            # Print the readers in the list.
            if len(readers) > 0:
                for reader in readers:
                    print(reader)
            else:
                print("There are no readers.")
        
main()
