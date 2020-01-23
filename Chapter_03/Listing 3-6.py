class Name():
    """A class to represent a person's name.

       Public methods: __init__, get_full_name,
                       get_initial_name
    """

    # Annotate object-level fields
    _full_name: str
    _initial_name: str
    
    def __init__(self,
                 first: str,
                 middle: str,
                 last: str)-> None:
        """Initialize full name and initial name fields."""
        self._full_name = first + " " + middle + " " + last
        self._initial_name = first[0] + ". " + last

    def get_full_name(self) -> str:
        """Return the full name."""
        return self._full_name

    def get_initial_name(self) -> str:
        """Return the name as first initial last name."""
        return self._initial_name
    
