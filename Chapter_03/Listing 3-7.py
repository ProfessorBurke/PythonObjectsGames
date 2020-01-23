"""Another client of the Name class."""
from Name import *

# Create a Name object.
hopper: Name = Name("Grace", "Brewster Murray", "Hopper")

# Invoke Name method.
print(hopper.get_first_last_name())
