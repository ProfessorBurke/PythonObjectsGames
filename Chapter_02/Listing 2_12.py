"""Demonstrate list operations in a card-dealing program."""

import random

def make_deck() -> list:
    """Create and return a standard 52-card deck."""
    # Annotate and initialize variables
    deck: list = []
    suit: str
    value: str

    # Iterate through suits and values to make cards.
    for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
        for value in ["Ace", "Two", "Three", "Four", "Five",
                      "Six", "Seven", "Eight", "Nine", "Ten",
                      "Jack", "Queen", "King"]:
            deck.append(value + " of " + suit)
    return deck

def main() -> None:
    """Make a deck, shuffle it, and deal."""
    # Annotate variables
    deck: list
    first_hand: list
    second_hand: list
    # Create and shuffle the deck.
    deck = make_deck()
    random.shuffle(deck)
    # Deal two five-card hands.
    first_hand = deck[:5]
    second_hand = deck[5:10]
    # Print the hands.
    print(first_hand)
    print(second_hand)

main()
