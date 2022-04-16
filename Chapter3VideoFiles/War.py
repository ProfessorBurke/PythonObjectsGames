from Deck import *

class War():
    """A game of war.

       Public methods:  __init__, play
    """

    # Annotate fields
    _deck: Deck
    _hand1: int
    _hand2: int

    def __init__(self) -> None:
        """Initialize a game of war."""
        self._deck = Deck()
        self._deck.shuffle()
        self._hand1 = self._deck.make_hand(5)
        self._hand2 = self._deck.make_hand(5)

    def play(self) -> None:
        """Play a game of war."""
        print(self._deck.show_top_card(self._hand1))
        print(self._deck.show_top_card(self._hand2))



def main():
    war: War

    war = War()
    war.play()

main()
