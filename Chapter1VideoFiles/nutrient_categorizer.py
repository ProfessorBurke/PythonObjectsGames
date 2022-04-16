"""Categorize nutrient intake as low, ideal, acceptable, or high."""

# Annotate variables
nutrient: float

# Obtain the nutrient intake from the user.
nutrient = float(input("How much of the nutrient did you eat today? "))

# Determine and report the category.
if nutrient < 500:
    print("That intake is in the low category.")
elif nutrient < 1500:
    print("That intake is in the ideal category.")
elif nutrient < 2300:
    print("That intake is in the acceptable category.")
else:
    print("That intake is in the high category.")
