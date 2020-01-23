"""Manage a library summer reading program."""

# Define menu constants
ADD: int = 1
REMOVE: int = 2
VIEW_ALL: int = 3
QUIT: int = 4
MENU_TEXT: str = ("1. Add a reader\n2. Remove a reader\n" +
             "3. View all readers\n4. Quit")

def menu() -> int:
    """Obtain and return the user's menu choice."""
    choice: int = 0
    while choice < ADD or choice > QUIT:
        print(MENU_TEXT)
        choice = int(input("Please enter the number of "
                           + "your choice: "))
    return choice

def main() -> None:
    """Manage a list of readers."""
    # Annotate and initialize variables
    names: list = []
    choice: int = 0
    
    # Greet the user.
    print("Welcome!  How can I help you manage the "
          + "reading program?")

    # Process a menu choice.
    while choice != QUIT:
        choice = menu()
        if choice == ADD:
            # Obtain and add reader's name.
            name = input("What is the reader's name? ")
            names.append(name)
        elif choice == REMOVE:
            # Obtain reader's name.
            name = input("What is the reader's name? ")
            # Check to see if it's in the list and remove.
            if name in names:
                names.remove(name)
        elif choice == VIEW_ALL:
            # Print the list.
            print(names)
        
main()
