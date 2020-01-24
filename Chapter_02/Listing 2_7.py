"""Demonstrate scope."""

def func() -> None:
    """Define a function containing a function."""
    
    def inner_func() -> None:
        """Define a function within a function."""
        var1: int = 3
        print(var1, var2)
        
    # Declare some variables and call inner_func.
    var1: int = 1
    var2: int = 2
    inner_func()

def main() -> None:
    """Invoke a function."""
    func()

main()



