"""A program that searches for a word in text."""

def analyze_text(text: str, word: str) -> None:
    """Find occurrences of word in text."""
    # Annotate variables
    num_occurrences: int
    index1: int
    index2: int
    output: str = ""
    
    if word in text:
        # Word is in text, count occurrences.
        num_occurrences = text.count(word)
        output += "There are {} ".format(num_occurrences)
        output += "occurrences of {}. ".format(word)
        # Get the surrounding text and display.
        index = text.find(word)
        if num_occurrences > 1:
            # Rewrite to check indices with string length!
            index2 = text.find(word, index + len(word))
            output += "The first two are: \n"
            output += text[index-10:index+10]
            output += "\n"
            output += text[index2-10:index2+10]
        else:
            output += "It is: \n"
            output += text[index-10:index+10]
        print(output)
    else:
        output = "There are zero occurrences of "
        output += "{}.".format(word)
        print(output)

def main() -> None:
    text = ("The powers not delegated to the United States, "
            + "by the Constitution, nor prohibited by it to"
            + "the States, are reserved to the States "
            + "respectively, or to the people.")
    word = "States"
    analyze_text(text, word)

main()
