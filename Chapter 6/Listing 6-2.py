"""A more complicated example of saving program state
   with the pickle library."""

import pickle
import io

class Recipe:
    """A Recipe object represents a single recipe."""
    # Annotate object-level variables
    _ingredients: list
    _instructions: list

    def __init__(self, ingredients: list, instructions: list) -> None:
        """Initialize from parameters."""
        self._ingredients = ingredients
        self._instructions = instructions

    def __str__(self) -> str:
        """Return a string representing the recipe."""
        return str(self._ingredients) + "\n" + str(self._instructions)

class CookingSite:
    """Represent a single cooking website."""
    # Annotate object-level variables
    _url: str
    _name: str
    _review: str

    def __init__(self, url: str, name: str, review: str) -> None:
        """Initialize from parameters."""
        self._url = url
        self._name = name
        self._review = review

    def __str__(self) -> str:
        """Return a string representation of the cooking site."""
        return (self._name + "\n" + self._url + "\n" + self._review)

def main():
    """Demonstrate pickling more complicated data."""
    # Annotate variables
    file_out: io.BufferedWriter
    file_in: io.BufferedReader
    recipes: list
    websites: list

    # Create the program state.
    recipes = [Recipe(["box of cheesy mac", "water", "butter"],
                      ["Cook mac", "Add cheese and butter"]),
               Recipe(["frozen pizza", "vegetables"],
                      ["Cook pizza", "Make a salad out of veg"])]
    websites = [CookingSite("www.fastrecipes.com", "Fast Recipes",
                            "Fast!"),
                CookingSite("www.fancyrecipes.com", "Fancy Recipes",
                            "Fancy.")]

    # Display recipe and website data.
    for recipe in recipes:
        print(recipe)
    for website in websites:
        print(website)
    # Write recipe and website data to a binary file.
    with open("recipes", "wb") as file_out:
        pickle.dump(recipes, file_out)
        pickle.dump(websites, file_out)

    # Read recipe and website data from a binary file.
    with open("recipes", "rb") as file_in:
        recipes = pickle.load(file_in)
        websites = pickle.load(file_in)
    # Display recipe and website data.
    for recipe in recipes:
        print(recipe)
    for website in websites:
        print(website)

main()

    
