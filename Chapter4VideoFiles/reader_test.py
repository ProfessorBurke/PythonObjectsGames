"""Test the Reader class."""
from Reader import *

def main():
    """Create and print three Reader objects."""
    # Create three Reader objects.
    maya = Reader("Maya", 100)
    sherman = Reader("Sherman", 200)
    anton = Reader("Anton", 50)

    # Print three reader objects.
    print(maya)
    print(sherman)
    print(anton)

main()
