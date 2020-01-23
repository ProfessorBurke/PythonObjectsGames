"""Illustrate the iterator pattern with a row-major table."""

class TableIterator():
    """Iterate over a Table object.
       Public methods: __init__, __iter__, __next__
    """
    # Annotate object-level fields
    _table: "Table"
    _last_row: int
    _last_col: int
    _row: int
    _col: int

    def __init__(self, table: "Table", num_rows: int,
                 num_cols: int) -> None:
        """Initialize fields from parameters
        and set indices to first element."""
        self._table = table
        self._last_row = num_rows - 1
        self._last_col = num_cols - 1
        self._row = 0
        self._col = 0

    def __iter__(self) -> "TableIterator":
        """Return this object as the iterator."""
        return self

    def __next__(self) -> int:
        """Return the current element and increment indices
           or throw exception if out of elements."""
        # Annotate variable
        item: int
        # Check to see if we're done and raise exception.
        if self._row == self._last_row + 1:
            raise StopIteration
        # If we're still here, get item and increment indices.
        item = self._table[(self._row, self._col)]
        if self._col == self._last_col:
            self._row += 1
            self._col = 0
        else:
            self._col += 1
        # Return the item.
        return item
    
class Table():
    """Manage a row-major table of integers.
       Public methods: __init__, __iter__, __getitem__
    """

    # Annotate object-level fields
    _data: list

    def __init__(self, data: list) -> None:
        """Initialize field from parameter.
           data is a 2d list of at least one row."""
        self._data = data

    def __getitem__(self, indices: tuple) -> int:
        """Return item at index indices[0], indices[1]."""
        return self._data[indices[0]][indices[1]]

    def __iter__(self) -> TableIterator:
        """Return an iterator."""
        return TableIterator(self,
                             len(self._data),
                             len(self._data[0]))

def main():
    """Create a table and iterate over it."""
    # Annotate variables
    table: Table
    item: int
    
    table = Table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    for item in table:
        print(item)

main()
