class Reader():
    """A class representing a participant in the
       library reading program.

       Public methods:  __init__, get_name, get_total_minutes,
                       add_minutes, __str__
    """

    # Annotate object-level fields
    _name: str
    _minutes: list
    
    def __init__(self, name: str, minutes_read: int = 0) -> None:
        """Initialize a Reader with name and minutes."""
        self._name = name
        self._minutes = []
        if minutes_read != 0:
            self._minutes.append(minutes_read)

    def get_name(self) -> str:
        """Return the reader's name."""
        return self._name

    def get_total_minutes(self) -> str:
        """Return the total minutes read."""
        return sum(self._minutes)

    def add_minutes(self, minutes_read: int) -> None:
        """Add minutes_read to minutes."""
        self._minutes.append(minutes_read)

    def __str__(self) -> str:
        """Return a string version of the reader."""
        name_str: str = "Name: " + self._name
        minutes_str: str = ("Minutes: "
                            + str(self.get_total_minutes()))
        return name_str + "\n" + minutes_str
