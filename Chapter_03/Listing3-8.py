class Name():
    """A class to represent a person's name.

       Public methods: __init__, get_full_name,
                       get_initial_name, get_first_last_name
    """

    # Annotate object-level fields
    _first: str
    _middle: str
    _last: str
    
    def __init__(self,
                 first: str,
                 middle: str,
                 last: str) -> None:
        """Initialize full name and initial name fields."""
        self._first = first
        self._middle = middle
        self._last = last

    def get_full_name(self) -> str:
        """Return the full name."""
        return (self._first + " " + self._middle
                + " " + self._last)

    def get_initial_name(self) -> str:
        """Return the name as first initial last name."""
        return self._first[0] + ". " + self._last

    def get_first_last_name(self) -> str:
        """Return the name as first initial last name."""
        return self._first + " " + self._last

    
