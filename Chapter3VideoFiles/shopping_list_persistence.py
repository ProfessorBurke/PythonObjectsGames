from ShoppingList import *

def main():
    """Create instances of the ShoppingList class."""

    # Annotate variables.
    list1: ShoppingList
    list2: ShoppingList
    list3: ShoppingList

    list1 = ShoppingList()
    list2 = ShoppingList()
    list3 = list2

    list1.add_item("tabbouleh")
    list2.add_item("scallop maki")

    list2 = ShoppingList()
    list1 = ShoppingList()

main()
