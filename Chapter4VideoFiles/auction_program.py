"""Part of an auction program."""

class Bid():
    """ A class to represent a single bid."""

    # Annotate object-level fields
    _bid_value: float
    _account: "Account"
    _listing: "Listing"

    def __init__(self, value: float, account: "Account", listing: "Listing") -> None:
        """Initialize fields from parameters."""
        self._bid_value = value
        self._account = account
        self._listing = list

    def get_value(self) -> float:
        """Return the value of the bid."""
        return self._bid_value

class Listing():
    """A class to represent an auction listing."""

    # Annotate object-level fields
    _name: str
    _description: str
    _minimum_bid_value: float
    _current_high_bid: Bid

    def __init__(self, name: str, description: str, minimum_bid_value: float) -> None:
        """Initialize fields from parameters, set current bid to None."""
        self._name = name
        self._description = description
        self._minimum_bid_value = minimum_bid_value
        self._current_high_bid = None

    def get_view(self) -> str:
        """Return a string view of the listing."""
        return self._name + "\n" + self._description

    def get_current_high_bid(self) -> Bid:
        """Return the current high bid."""
        return self._current_high_bid

    def get_minimum_start_value(self) -> float:
        """Return the minimum starting bid."""
        return self._minimum_bid_value

    def set_high_bid(self, bid:Bid) -> None:
        """Set the high bid to the parameter."""
        self._current_high_bid = bid

class Account():
    """Represent an account in the system."""

    # Annotate object-level fields
    _name: str
    _id: int
    _bids: list
    _listings: list
    _auctioneer: "Auctioneer"

    def __init__(self, name: str, id: int, auctioneer: "Auctioneer") -> None:
        """Initialize an account from parameters with empty bids and listings."""
        self._name = name
        self._id = id
        self._auctioneer = auctioneer
        self._listings = []
        self._bids = []

    def add_bid(self, bid: Bid) -> None:
        """Add the bid to the bids."""
        self._bids.append(bid)


class Auctioneer():
    """Manage auction rules."""

    def bid(self, listing: Listing, bid_value: float, account: Account) -> bool:
        """Process a bid request."""
        # Annotate variables
        current_high_bid: Bid
        minimum_starting_value: float
        current_bid_value: float
        high_bid: Bid
        bid_is_high_bid: bool = False

        current_high_bid = listing.get_current_high_bid()
        if current_high_bid == None:
            minimum_starting_value = listing.get_minimum_start_value()
            bid_is_high_bid = bid_value >= minimum_starting_value
        else:
            current_bid_value = current_high_bid.get_value()
            bid_is_high_bid = bid_value > current_bid_value

        if bid_is_high_bid:
            high_bid = Bid(bid_value, account, listing)
            listing.set_high_bid(high_bid)
            account.add_bid(high_bid)

        return bid_is_high_bid


def main():
    # Annotate and initialize variables
    auctioneer: Auctioneer = Auctioneer()
    arduino_kid: Account = Account("Arduino Kid", 12345, auctioneer)
    toy_lot: Listing = Listing("Toy lot", "A lot of RC and electronic toys suitable for mods.", .02)

    print(toy_lot.get_view() + "\n")
    
    result = "Bidding on the toy lot for .01 was "
    if auctioneer.bid(toy_lot, .01, arduino_kid,):
        print(result + "a success.")
    else:
        print(result + "a failure.\n")
    result = "Bidding on the toy lot for .02 was "
    if auctioneer.bid(toy_lot, .02, arduino_kid):
        print(result + "a success.")
    else:
        print(result + "a failure.\n")        
    result = "Bidding on the toy lot for .01 was "
    if auctioneer.bid(toy_lot, .01, arduino_kid):
        print(result + "a success.")
    else:
        print(result + "a failure.\n")
    result = "Bidding on the toy lot for .04 was "
    if auctioneer.bid(toy_lot, .04, arduino_kid):
        print(result + "a success.")
    else:
        print(result + "a failure.\n")  


main()



        





    
