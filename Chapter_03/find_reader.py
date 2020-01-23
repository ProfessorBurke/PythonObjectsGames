from Reader import *

def find_reader(name: str, readers: list) -> Reader:
    """Return the object with name passed."""
    reader: Reader = None
    found: bool = False
    i: int = 0
    while not found and i < len(readers):
        if readers[i].get_name() == name:
            found = True
            reader = readers[i]
        i += 1
    return reader
