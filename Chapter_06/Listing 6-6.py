"""Manage a library summer reading program."""
import copy

class Reader():
    """A class representing a participant in the
       library reading program.

       Public methods:  __init__, get_name, get_total_minutes,
                       add_minutes, __str__
    """

    # Annotate object-level fields
    _name: str
    _minutes: list
    
    def __init__(self, name: str, minutes_read: int = 0) -> None:
        """Initialize a Reader with name and minutes."""
        self._name = name
        self._minutes = []
        if minutes_read != 0:
            self._minutes.append(minutes_read)

    def get_name(self) -> str:
        """Return the reader's name."""
        return self._name

    def get_total_minutes(self) -> str:
        """Return the total minutes read."""
        return sum(self._minutes)

    def add_minutes(self, minutes_read: int) -> None:
        """Add minutes_read to minutes."""
        self._minutes.append(minutes_read)

    def __str__(self) -> str:
        """Return a string version of the reader."""
        name_str: str = "Name: " + self._name
        minutes_str: str = ("Minutes: "
                            + str(self.get_total_minutes()))
        return name_str + "\n" + minutes_str

class ReaderManager():
    """A class that manages the list of readers.

       Public methods:  __init__, add_reader, remove_reader,
                        display_readers
    """

    # Annotate object-level fields
    _readers: list

    def __init__(self) -> None:
        """Create an empty list for Reader objects."""
        self._readers = []

    def add_reader(self, reader) -> None:
        """Add a Reader object to the list."""
        self._readers.append(reader)

    def remove_reader(self, reader) -> None:
        """Remove a Reader object from the list."""
        self._readers.remove(reader)

    def display_readers(self) -> None:
        """Display all Reader objects in the list."""
        if len(self._readers) > 0:
            for reader in self._readers:
                print(reader)
        else:
            print("There are no readers.")

class Command():
    """Abstract superclass for command structure.

       Public methods:  __init__, execute, undo
    """

    # Annotate object-level fields
    _executor: object
    
    def __init__(self, executor: object) -> None:
        """Initialize from parameter."""
        self._executor = executor

    def execute(self) -> None:
        """Execute the command."""
        pass

    def undo(self) -> None:
        """Undo the command."""
        pass

class QuitCommand(Command):
    """A command to quit the program.

       Public methods:  __init__, execute
    """

    #_executor: Menu
    def execute(self) -> None:
        self._executor.quit()

class AddCommand(Command):
    """A command to add a reader or undo.

       Public methods:  __init__, execute, undo
    """

    # Annotate object-level fields
    _reader: Reader
    #_executor: ReaderManager

    def __init__(self, executor: object) -> None:
        """Initialize from parameter."""
        super().__init__(executor)
        self._reader = None

    def execute(self) -> None:
        """Create a Reader and add to the list."""
        # Annotate variables.
        name: str
        has_minutes: str
        minutes: int
        
        # Create a reader.
        if not self._reader:
            name = input("What is the child's name? ")
            has_minutes = input("Has the child read? (Y or N) ")
            if has_minutes == "Y":
                minutes = int(input("How many minutes? "))
                self._reader = Reader(name, minutes)
            else:
                self._reader = Reader(name)
                
        # Ask the executor to add the reader.
        self._executor.add_reader(self._reader)

    def undo(self) -> None:
        """Remove the reader from the list."""
        # Ask the executor to remove the reader.
        self._executor.remove_reader(self._reader)


class ViewAllCommand(Command):
    """A command to view all readers.

       Public methods:  __init__, execute
    """
    #_executor: ReaderManager
    
    def execute(self) -> None:
        """Show all readers."""
        self._executor.display_readers()

class UndoCommand(Command):
    """A command to undo the last command.

       Public methods:  __init__, execute
    """

    #_executor: Menu
    def execute(self) -> None:
        """Undo the last undoable command."""
        self._executor.undo_last_command()


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

class UndoableMenuItem(MenuItem):
    """A MenuItem that can be undone.

       Public methods:  action
    """
    
    def action(self):
        command_copy = copy.copy(self._command)
        command_copy.execute()
        return command_copy
        
class Menu():
    """The loop that drives the program through a text menu.
       There should be only one Menu per program.

       Public methods:  __init__, go, quit
    """
        
    # Annotate object-level fields
    _menu_items: list
    _undoable_commands: list
    _quit: bool = False
    
    def __init__(self) -> None:
        """Initialize Menu object and create menu."""
        self._menu_items = []
        self._undoable_commands = []

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

    def undo_last_command(self) -> None:
        """Undo the last command, if any."""
        num_commands = len(self._undoable_commands)
        if  num_commands > 0:
            last_command = self._undoable_commands[-1]
            last_command.undo()
            self._undoable_commands.remove(last_command)
        else:
            print("There are no undoable commands.")
        
    def quit(self) -> None:
        """Quit the program."""
        self._quit = True
    
    def go(self) -> None:
        """Display menu and process choices until quit."""
        # Annotate and initialize variable
        choice: int = 0
        new_command: Command
        while not self._quit:
            choice = self._show_menu()
            new_command = self._menu_items[choice - 1].action()
            if new_command:
                self._undoable_commands.append(new_command)
                
def main() -> None:
    """Create the menu and go."""
    # Annotate constants
    ADD: str = "Add a reader"
    VIEW: str = "View all readers"
    UNDO: str = "Undo last command"
    QUIT: str = "Quit"

    # Annotate and initialize variables
    menu: Menu = Menu()
    reader_manager: ReaderManager = ReaderManager()
    
    menu.add_menu_item(UndoableMenuItem(ADD, AddCommand(reader_manager)))
    menu.add_menu_item(MenuItem(VIEW, ViewAllCommand(reader_manager)))
    menu.add_menu_item(MenuItem(UNDO, UndoCommand(menu)))
    menu.add_menu_item(MenuItem(QUIT, QuitCommand(menu)))
    menu.go()
        
main()
