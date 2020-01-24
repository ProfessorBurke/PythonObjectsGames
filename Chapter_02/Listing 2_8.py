"""Demonstrate scope."""

def func() -> None:
    """Demonstrate scope error."""
    print(var)
    var: int = 5

# Module-level scope.
var: int = 10
func()



