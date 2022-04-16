"""Calculate weight on Mars."""

### Annotate variables
##weight: float
##mars_weight: float
##
### Obtain weight from the user.
##weight = float(input("What is the weight on Earth? "))
##
### Compute weight on Mars.
##mars_weight = weight / 9.8 * 3.7
##
### Display the weight on mars.
##print("An object that weights {:.1f} lb on Earth will weigh {:.1f} lb on Mars.".format(weight, mars_weight))

# Print a table.
print("{:<10s}{:<10s}".format("Earth", "Mars"))
print("{:<10.1f}{:<10.1f}".format(20, 20/9.8*3.7))
print("{:<10.1f}{:<10.1f}".format(40, 40/9.8*3.7))
print("{:<10.1f}{:<10.1f}".format(60, 60/9.8*3.7))
