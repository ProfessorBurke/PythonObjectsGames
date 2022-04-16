"""Create parallel lists of readers and minutes read."""

def main() -> None:
    """Create and print two parallel lists."""
    # Annotate variables
    readers: list = []
    minutes: list = []
    i: int = 0
    name: str
    minutes_read: int

    while i < 5:
        name = input("What is the child's name? ")
        minutes_read = int(input("How many minutes did " + name + " read? "))
        readers.append(name)
        minutes.append(minutes_read)
        
        i += 1
    print(readers)
    print(minutes)



main()
