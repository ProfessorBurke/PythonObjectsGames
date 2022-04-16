from typing import ClassVar

class Stamp():
    """A passport stamp in the library reading program.

       Public methods: __init__, get_value, get_cost,
                       __str__
    """

    # Annotating object-level fields
    _value: str
    _cost: int

    def __init__(self, value: str, cost: int) -> None:
        """Initialize fields with parameters."""
        self._value = value
        self._cost = cost

    def get_value(self) -> str:
        """Return the value of the stamp."""
        return self._value

    def get_cost(self) -> int:
        """Return the cost of the stamp."""
        return self._cost

    def __str__(self) -> str:
        """Return a string version of the stamp."""
        return "{:<15s}{:<d}".format(self._value, self._cost)


class StampManager():
    """Manage the stamps in the library reading program.

       Public methods: get_stamp_cost, get_empty_stamp
    """

    # Annotating and initializing class-level fields
    _stamp_cost: ClassVar[int] = 90
    _empty_stamp: ClassVar[Stamp] = Stamp("Empty stamp",
                                          _stamp_cost)
    _stamps: ClassVar[list] = [Stamp("Superstar", _stamp_cost),
               Stamp("Bookworm", _stamp_cost),
               Stamp("Nonfiction Rules!", _stamp_cost)]

    def get_stamp_cost(self) -> int:
        """Return the cost of a stamp."""
        return StampManager._stamp_cost

    def get_empty_stamp(self) -> Stamp:
        """Return a reference to the empty stamp."""
        return StampManager._empty_stamp
    


class Passport():
    """Manage a passport in the reading program.

       Public methods: __init__, request_stamp, __str__
    """

    # Annotating object-level fields
    _stamps: list
    _stamp_manager: StampManager

    def __init__(self, stamp_manager: StampManager) -> None:
        """Initialize passport from parameters."""
        self._stamps = []
        self._stamp_manager = stamp_manager

    def request_stamp(self, reader_account: "ReaderAccount") -> bool:
        """Return true if stamp request is accepted, false otherwise."""
        # Annotate and initialize variables
        success: bool = False
        cost: int
        free_minutes: int
        stamp: Stamp

        # Fulfill stamp request and return success.
        cost = self._stamp_manager.get_stamp_cost()
        free_minutes = reader_account.get_free_minutes()
        if free_minutes >= cost:
            stamp = self._stamp_manager.get_empty_stamp()
            self._stamps.insert(0, stamp)
            reader_account.deduct_free_minutes(cost)
            success = True
        return success

    def __str__(self) -> str:
        """Return a string version of the passport."""
        stamp_str: str = ""
        if len(self._stamps) > 0:
            for stamp in self._stamps:
                stamp_str += str(stamp) + "\t"
        else:
            stamp_str = "No stamps in passport"
        return stamp_str
        
        
class ReaderAccount():
    """Manage a Reader's reading program account.
       Public methods: __init__, get_free_minutes,
                       log_minutes, deduct_free_minutes,
                       request_stamp, __str__
    """

    # Annotating object-level fields
    _reader_id: int
    _name: str
    _free_minutes: int
    _passport: Passport

    def __init__(self,
                 reader_id: int,
                 name: str,
                 stamp_manager: StampManager) -> None:
        """Initialize reader account from parameters."""
        self._reader_id = reader_id
        self._name = name
        self._free_minutes = 0
        self._passport = Passport(stamp_manager)

    def get_free_minutes(self) -> int:
        """Return the number of free minutes."""
        return self._free_minutes

    def log_minutes(self, minutes: int) -> None:
        """Add parameter minutes to log."""
        self._free_minutes += minutes

    def deduct_free_minutes(self, minutes: int) -> None:
        """Deduct parameter minutes from log."""
        self._free_minutes -= minutes

    def request_stamp(self) -> bool:
        """Request a stamp for accumulated minutes."""
        success: bool = self._passport.request_stamp(self)
        return success

    def __str__(self) -> str:
        """Return a string version of the reader account."""
        return ("{:<10s}{:<10d}{}\n".format(self._name,
                                            self._reader_id,
                                            self._free_minutes)
                + str(self._passport))



def main() -> None:
    """Test the request passport stamp use case."""
    # Annotate variables
    manager: StampManager
    reader1: ReaderAccount
    reader2: ReaderAccount
    success: bool
    
    # Make one StampManager
    manager = StampManager()

    # Make two ReaderAccounts
    reader1 = ReaderAccount(112233, "D.Knuth", manager)
    reader2 = ReaderAccount(445566, "G.Hopper", manager)

    print("Reader 1 does not log enough minutes:")
    reader1.log_minutes(60)
    print(reader1)
    success = reader1.request_stamp()
    print("Successful stamp request: " + str(success))
    print(reader1)
    
    print("\nReader 2 logs enough minutes: ")
    reader2.log_minutes(90)
    print(reader2)
    success = reader2.request_stamp()
    print("Successful stamp request: " + str(success))
    print(reader2)

    print("\nReader 1 logs enough minutes: ")
    reader1.log_minutes(60)
    print(reader1)
    success = reader1.request_stamp()
    print("Successful stamp request: " + str(success))
    print(reader1)


main()
