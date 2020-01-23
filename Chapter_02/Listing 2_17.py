"""A small table demonstrating format specifiers."""

def print_table() -> None:
    """Print a table of data."""
    # Print the header
    print("{:<15s}{:<15s}{:<15s}".format("Video name",
                                         "Retention",
                                         "Likes"))
    print("{:<15s}{:<15.1f}{:<15,d}".format("Cat likes box",
                                             65.2,
                                             1426983))
    print("{:<15s}{:<15.1%}{:<15,d}".format("Epic fail",
                                             .976,
                                             20059841))

print_table()
