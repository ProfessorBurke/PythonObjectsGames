"""Create a shopping list, add and remove items."""

from ShoppingList import *

def main() -> None:
    """Demonstrate the ShoppingList class."""

    # Create a shopping list and add some items.
    my_list = ShoppingList()
    my_list.add_item("milk")
    my_list.add_item("bread")
    my_list.add_item("peanut butter")

    # Show the list and the all items list.
    print("List: " + str(my_list.get_list()))
    print("All items: " + str(my_list.get_all_items()))

    # Remove and add the same item, remove another item.
    my_list.remove_item("bread")
    my_list.add_item("bread")
    my_list.remove_item("milk")

    # Show the list and the all items list.
    print("List: " + str(my_list.get_list()))
    print("All items: " + str(my_list.get_all_items()))

main()    
