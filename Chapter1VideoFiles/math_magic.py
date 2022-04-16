"""Perform a magic trick with math."""

# Annotate variables.
num: int
next_num: float

# Obtain a value from the user
num = int(input("Think of a number between 1 and 100 and type it here: "))

# Calculate the new value at each step and show the user.
next_num = num * 3
input("Multiply by 3 and press enter when you're done...")
print("You should have gotten " + str(next_num))

next_num = next_num + 15
input("Add 15 and press enter when you're done...")
print("You should have gotten " + str(next_num))

next_num = next_num * 2
input("Multiply by 2 and press enter when you're done...")
print("You should have gotten " + str(next_num))

next_num = next_num + 12
input("Add 12 and press enter when you're done...")
print("You should have gotten " + str(next_num))

next_num = next_num // 6
input("Divide by 6 and press enter when you're done...")
print("You should have gotten " + str(next_num))

next_num = next_num - num
input("Subtract your original number and press enter for the result...")

# Show the result.
print("You got 7!")
