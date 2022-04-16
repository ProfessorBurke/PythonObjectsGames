import random

class Deck():
    """A class representing a standard deck of 52 cards.
       Public methods:  __init__, shuffle, make_hand,
       show_top_card
    """

    # Annotate object-level fields
    _hands: dict
    _stock: list

    def _get_card_name(self, card: int) -> str:
        """Convert the card to a string representation."""
        suits: list = ["hearts", "clubs", "diamonds", "spades"]
        ranks: list = ["ace", "two", "three", "four", "five", "six", "seven",
                 "eight", "nine", "ten", "jack", "queen", "king"]
        return ranks[card % 13] + " of " + suits[card // 13]

    def __init__(self) -> None:
        """Create a standard 52-card deck."""
        self._hands = {}
        self._stock = list(range(51))

    def shuffle(self) -> None:
        """Shuffle the stock."""
        random.shuffle(self._stock)

    def make_hand(self, size: int) -> int:
        """Create a hand of size cards and return a key."""
        key: int = len(self._hands)
        hand: list = []
        for i in range(size):
            hand.append(self._stock[i])
            self._stock = self._stock[1:]
        self._hands[key] = hand
        return key

    def show_top_card(self, key: int = -1) -> str:
        """Return a string representing the top card of the hand with key."""
        hand: str
        if key != -1:
            hand = self._get_card_name(self._hands[key][0])
        else:
            hand = self._get_card_name(self._stock[0])
        return hand
        
