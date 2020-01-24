"""Demonstrate scope."""

def func(param: int) -> None:
    """Define a function with a parameter and
       two local variables."""
    var: int = 0
    var2: int = 0
    print("\nIn func: ")
    print("\tvar: " + str(var))
    print("\tvar2: " + str(var2))
    print("\tparam: " + str(param))

# This code is at the module level.
var: int = 10
print("In module: ")
print("\tvar: " + str(var))
func(var)
