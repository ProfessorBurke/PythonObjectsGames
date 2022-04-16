"""Pre-process floating-point data."""

def remove_na(pre_list: list) -> None:
    """Remove all 'NA' values from the parameter list."""
    while "NA" in pre_list:
        pre_list.remove("NA")

def main() -> None:
    """Demonstrate a function that modifies a parameter."""
    # Define and display a list.
    data: list = [1.23, "NA", 1.15, .98, "NA", 1.02, "NA"]
    print(data)
    # Pass the list to a function and display again.
    remove_na(data)
    print(data)

main()
