"""Pre-process floating-point data."""

def remove_na(data: list) -> None:
    """Remove all 'NA' values from the parameter list."""
    while "NA" in data:
        data.remove("NA")

def main() -> None:
    """Copy a list before passing it to a function."""
    # Define, copy, and display a list.
    data: list = [1.23, "NA", 1.15, .98, "NA", 1.02, "NA"]
    processed_data: list = data.copy()
    print(data)
    # Pass the copy to a function and display again.
    remove_na(processed_data)
    print(data)
    print(processed_data)

main()
