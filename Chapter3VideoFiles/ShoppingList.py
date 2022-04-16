class ShoppingList():
    """A class representing a shopping list.

       Public methods:  __init__, add_item, remove_item,
                        get_list, get_all_items
    """

    # Annotate object-level fields
    _items: list
    _all_items: list

    def __init__(self) -> None:
        """Initialize an empty instance of ShoppingList."""
        self._items = []
        self._all_items = []

    def add_item(self, item: str) -> None:
        """Add item to list and to all items list."""
        self._items.append(item)
        if not item in self._all_items:
            self._all_items.append(item)

    def remove_item(self, item: str) -> None:
        """Remove item from the shopping list."""
        if item in self._items:
            self._items.remove(item)

    def get_list(self) -> list:
        """Return a copy of the shopping list."""
        return self._items.copy()

    def get_all_items(self) -> list:
        """Return a copy of all items list."""
        return self._all_items.copy()

    def get_num_items(self) -> int:
        """Return the number of items on the shopping list."""
        return len(self._items)

    def __str__(self) -> str:
        """Return a string version of the list."""
        output: str = "Items: "
        output += str(self._items)
        output += "\nAll items: " + str(self._all_items)
        return output
    
    
