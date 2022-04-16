"""A book review program."""

class Book():
    """A class representing a book.

       Public methods:  __init__, __str__
    """

    # Annotate object-level fields
    _title: str
    _author: str
    
    def __init__(self, title: str, author: str) -> None:
        """Create a Book with title and author."""
        self._title = title
        self._author = author

    def __str__(self) -> str:
        """Return a string description of the book."""
        return self._title + " by " + self._author

class Reader():
    """A class representing a library reader.

       Public methods:  __init__, __str__
    """

    # Annotate object-level fields
    _name: str
    _card_number: int

    def __init__(self, name: str, card_number: int) -> None:
        """Create a Reader with name and card number."""
        self._name = name
        self._card_number = card_number

    def __str__(self) -> str:
        """Return a string description of the reader."""
        return self._name + ", " + str(self._card_number)

class Review():
    """A class representing a book review.

       Public methods:  __init__, __str__
    """

    # Annotate object-level fields
    _reviewer: Reader
    _book: Book
    _rating: int
    _review: str

    def __init__(self,
                 reader: Reader,
                 book: Book,
                 rating: int,
                 review: str) -> None:
        """Create a Review with parameters passed."""
        self._reviewer = reader
        self._book = book
        self._rating = rating
        self._review = review

    def __str__(self) -> str:
        """Return a string describing the review."""
        return "{:15}{}\n{:15}{}\n{:15}{}\n{:15}{}".format(
            "Review of:", str(self._book), "By:",
            str(self._reviewer), "Rating:", str(self._rating),
            "Review", self._review)

def main() -> None:
    """Demonstrate the Book, Review, and Reader classes."""
    # Annotate variables
    book: Book
    reader_tim: Reader
    reader_john: Reader
    review_tim: Review
    review_john: Review
    
    # Create a book and two readers.
    book = Book("Palindromemordnilap", "Hannah Nolon")
    reader_tim = Reader("Tim Smit", 100226843)
    reader_john = Reader("John Lincoln", 100235178)
    
    # Create two reviews of the same book.
    review_tim = Review(reader_tim, book, 5,
                        "Loved it! I'll never read only forward again!")
    review_john = Review(reader_john, book, 1,
                         "Book was twice as long as I expected.")

    # Print the reviews.
    print(review_tim)
    print(review_john)

main()
