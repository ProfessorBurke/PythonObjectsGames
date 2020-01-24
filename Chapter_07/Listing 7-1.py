"""A calendar, purchase and subscription program,
   to illustrate multiple inheritance.
"""
from datetime import date

class Calendar():
    pass

class Cart():
    pass

class CalendarItem():
    """Represent one item in a calendar.

       Public methods:  __init__, __str__, activate
    """

    # Annotate object-level fields
    _date: date
    _name: str
    _calendar: Calendar

    def __init__(self, item_date: date,
                 name: str, calendar: Calendar, **kwargs) -> None:
        """Initialize fields from parameters."""
        super().__init__(**kwargs)
        self._date = item_date
        self._name = name
        self._calendar = Calendar

    def activate(self) -> None:
        """Take necessary action as item date is now."""
        pass

    def __str__(self) -> str:
        """Return a string version of the calendar item."""
        return (str(self._date) + "\n"
                + self._name + "\n")

class Purchase():
    """Represent a purchase.

       Public methods: __init__, __str__, add_to_cart
    """

    # Annotate object-level fields
    _item: str
    _description: str
    _cost: float
    _cart: Cart
                
    def __init__(self, item: str, description: str, cost: float, cart: Cart, **kwargs) -> None:
        """Initialize fields from parameters."""
        print(kwargs)
        super().__init__(**kwargs)
        self._item = item
        self._description = description
        self._cost = cost
        self._cart = cart

    def add_to_cart(self) -> None:
        """Item is being purchased; add to cart."""
        pass

    def __str__(self) -> str:
        """Return a string version of the purchase."""
        return (super().__str__() + self._item + "\n" + self._description + "\n"
                + "${:.2f}".format(self._cost))

class Subscription(Purchase, CalendarItem):
    """Represent a subscription.

       Public methods: __init__, __str__, activate
    """

    # Annotate object-level fields
    _frequency: int
                
    def __init__(self, frequency: int, **kwargs) -> None:
        """Initialize fields from parameters."""
        super().__init__(**kwargs)
        self._frequency = frequency

    def activate(self) -> None:
        """Add self to cart and create a copy one _frequency interval
           in the future and add to calendar."""
        # Add self to cart
        # Copy self with date _frequency in the future
        # Add self to calendar

    def __str__(self) -> str:
        """Return a string version of the subscription."""
        return (super().__str__() + "\n"
                + "Every " + str(self._frequency) + " month(s)")

def main():
    """Create and print a Subscription object."""
    subscribe = Subscription(frequency = 1,
                             item = "coffee",
                             description = "2 lb French roast",
                             name = "place coffee order",
                             item_date = date(2019, 1, 1),
                             cost = 50.0,
                             cart = Cart(), calendar = Calendar())

    print(subscribe)

main()
   
