
class DataSetIter():
    """An iterator that will skip none codes in a data set.

       Public methods:  __init__, __iter__, __next__
    """

    # Annotate object-level fields
    _data_set: "DataSet"
    _none_code: str
    _next: int
    _last: int

    def __init__(self, data_set: "DataSet", length: int, none_code: str) -> None:
        """Initialize from parameters and find first value in data."""
        self._data_set = data_set
        self._none_code = none_code
        self._last = length - 1
        self._next = 0
        while (self._next <= self._last
               and self._data_set[self._next] == self._none_code):
            self._next += 1
        
    def __iter__(self) -> "DataSetIter":
        """Return self as required."""
        return self

    def __next__(self) -> str:
        """Return the next data element or raise exception."""
        # Annotate variable
        data: str
        if self._next > self._last:
            raise StopIteration
        else:
            data = self._data_set[self._next]
            self._next += 1
            while (self._next <= self._last
                   and self._data_set[self._next] == self._none_code):
                self._next += 1
            
        return data
    
class DataSet():
    """A data set with none codes for missing entries.

       Public methods:  __init__, __iter__, __getitem__
    """

    # Annotate object-level variables.
    _data: list
    _none_code: str

    def __init__(self, data: list, none_code: str) -> None:
        """Initialize from parameters."""
        self._data = data
        self._none_code = none_code

    def __iter__(self) -> DataSetIter:
        """Return an iterator."""
        return DataSetIter(self, len(self._data), self._none_code)

    def __getitem__(self, index: int) -> str:
        """Return the item in _data at index."""
        return self._data[index]
        

def main():
    """Test the DataSetIterator."""
    # Annotate variables
    data: DataSet
    element: str
    
    # Testing NA at the end
    print("*********************************")
    print("Testing none code at the end.")
    print("Test: A, NA, B, A, NA, NA")
    print("Expected output A, B, A")
    data = DataSet(["A", "NA", "B", "A", "NA", "NA"], "NA")
    for element in data:
        print(element)

    # Testing NA at the beginning
    print("*********************************")
    print("Testing none code at the beginning.")
    print("Test: NA, A, NA, B, A, NA, NA")
    print("Expected output A, B, A")
    data = DataSet(["NA", "A", "NA", "B", "A", "NA", "NA"], "NA")
    for element in data:
        print(element)

    # Testing only NA
    print("*********************************")
    print("Testing only none code.")
    print("Test: NA")
    print("Expected output ")
    data = DataSet(["NA"], "NA")
    for element in data:
        print(element)

    # Testing only one non-NA
    print("*********************************")
    print("Testing no none code, only one item.")
    print("Expected output A")
    data = DataSet(["A"], "NA")
    for element in data:
        print(element)

    # One item after NA
    print("*********************************")
    print("Testing none code and only one item.")
    print("Test: NA, A")
    print("Expected output A")
    data = DataSet(["NA", "A"], "NA")
    for element in data:
        print(element)

    # All NA
    print("*********************************")
    print("Testing all none code.")
    print("Test: NA, NA, NA")
    print("Expected output ")
    data = DataSet(["NA", "NA", "NA"], "NA")
    for element in data:
        print(element)

    # Empty list
    print("*********************************")
    print("Testing empty list.")
    print("Test: ")
    print("Expected output ")
    data = DataSet([], "NA")
    for element in data:
        print(element)

    # Iterate over the DataSet without for..in
    # Annotate a variable for this demonstration
    done: bool = False
    data_iter: DataSetIter
    
    data = DataSet(["NA", "A", "NA", "B", "A", "NA", "NA"], "NA")
    data_iter = iter(data)
    
    while not done:
        try:
            element = next(data_iter)
            print(element)
        except StopIteration:
            done = True
        
main()
    
    
