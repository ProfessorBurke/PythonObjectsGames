"""A simplified calendar, purchase and subscription program,
   to illustrate naming conflicts.
"""

class CalendarItem():
    """Represent one item in a calendar.

       Public methods:  __init__, duplicate, overridden
    """

    # Annotate object-level fields
    name: str

    def __init__(self) -> None:
        """Initialize fields from parameters."""
        self.name = "calendar_item"

    def duplicate(self) -> None:
        print("In CalendarItem duplicate.")

    def overridden(self) -> None:
        print("In CalendarItem overridden.")

class Purchase():
    """Represent a purchase.

       Public methods: __init__, duplicate, overridden
    """

    # Annotate object-level fields
    name: str
                
    def __init__(self) -> None:
        """Initialize fields from parameters."""
        self.name = "purchase"

    def duplicate(self) -> None:
        print("In Purchase duplicate.")

    def overridden(self) -> None:
        print("In Purchase overridden.")

class Subscription(Purchase, CalendarItem):
    """Represent a subscription.

       Public methods: __init__, overridden
    """

    def __init__(self) -> None:
        """Initialize fields from parameters."""
        super().__init__()

##    def overridden(self) -> None:
##        super().overridden()
##        print("In Subscription overridden.")

    def overridden(self) -> None:
        CalendarItem.overridden(self)
        Purchase.overridden(self)
        print("In Subscription overridden.")

def main():
    """Create and print a Subscription object."""
    subscribe = Subscription()
    print(subscribe.name)
    subscribe.duplicate()
    subscribe.overridden()


main()
   
