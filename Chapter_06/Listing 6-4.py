"""Manage a library summer reading program."""

class Command():
    """Abstract superclass for command structure.

       Public methods:  __init__, execute, undo
    """

    # Annotate object-level fields
    _executor: object
    
    def __init__(self, executor: object) -> None:
        """Initialize from parameter."""
        self._executor = executor

    def execute(self):
        """Execute the command."""
        pass

class QuitCommand(Command):
    """A command to quit the program.

       Public methods:  __init__, execute, undo
    """

    #_executor: Menu
    def execute(self) -> None:
        self._executor.quit()

class MenuItem():
    """An Invoker object in the Command design pattern.

       Public methods:  __init__, get_text, action
    """

    # Annotate object-level fields
    _menu_text: str
    _command: object
    
    def __init__(self, menu_text: str, command: object) -> None:
        """Initialize a MenuItem from parameters."""
        self._menu_text = menu_text
        self._command = command

    def get_text(self) -> str:
        """Return the interface text."""
        return self._menu_text

    def action(self) -> object:
        """Execute the command."""
        self._command.execute()
        return None
        
class Menu():
    """The loop that drives the program through a text menu.
       There should be only one Menu per program.

       Public methods:  __init__, go, quit
    """
        
    # Annotate object-level fields
    _menu_items: list
    _quit: bool = False
    
    def __init__(self) -> None:
        """Initialize Menu object and create menu."""
        self._menu_items = []

    def _show_menu(self) -> int:
        """Obtain and return the user's menu choice."""
        # Annotate and initialize variable
        choice: int = 0
        while choice < 1 or choice > len(self._menu_items):
            for i in range(len(self._menu_items)):
                print(str(i + 1) + ". "
                      + self._menu_items[i].get_text())
            choice = int(input("Please enter the number of "
                               + "your choice: "))
        return choice

    def add_menu_item(self, menu_item: MenuItem) -> None:
        """Add the menu_item to the menu."""
        self._menu_items.append(menu_item)

    def remove_menu_item(self, menu_item: MenuItem) -> None:
        """Remove the menu_item from the menu."""
        if menu_item in self._menu_items:
            self._menu_items.remove(menu_item)
        
    def quit(self) -> None:
        """Quit the program."""
        self._quit = True
    
    def go(self) -> None:
        """Display menu and process choices until quit."""
        # Annotate and initialize variable
        choice: int = 0
        while not self._quit:
            choice = self._show_menu()
            new_command = self._menu_items[choice - 1].action()

def main() -> None:
    """Create the menu and go."""
    # Annotate constants
    ADD: str = "Add a reader"
    VIEW: str = "View all readers"
    QUIT: str = "Quit"

    menu: Menu = Menu()
    menu.add_menu_item(MenuItem(ADD, Command(menu)))
    menu.add_menu_item(MenuItem(VIEW, Command(menu)))
    menu.add_menu_item(MenuItem(QUIT, QuitCommand(menu)))
    menu.go()
        
main()
