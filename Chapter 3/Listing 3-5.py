"""Demonstrate using the Name class."""
from Name import *

# Create a Name object.
turing: Name = Name("Alan", "Mathison", "Turing")

# Invoke Name methods.
print(turing.get_full_name())
print(turing.get_initial_name())
