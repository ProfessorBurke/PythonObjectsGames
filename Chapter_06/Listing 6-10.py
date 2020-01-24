"""A simple observer example."""
import math

class Subject():
    """A Subject object represents something with a
       state change that will be reflected in other objects.

       Public methods: __init__, attach, detach, notify,
                       get_state, update_state
    """
    # Annotate object-level variables
    _state: int
    _observers: list

    def __init__(self) -> None:
        """Initialize state to zero and observers to empty list."""
        self._state = 0
        self._observers = []
    
    def attach(self, observer: object) -> None:
        """Attach an observer to this object."""
        self._observers.append(observer)

    def detach(self, observer: object) -> None:
        """Detach an observer from this object."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        """Notify observers that this object's state has changed."""
        for observer in self._observers:
            observer.update()

    def get_state(self) -> None:
        """Return state information about this object."""
        return self._state

    def update_state(self) -> None:
        """Update the state of this object."""
        self._state += 1
        self.notify()

class Observer():
    """An Observer object represents something that must
       update in response to a change in the subject.

       Public methods: __init__, update, get_state
    """
    # Annotate object-level variables
    _func: "function"
    _value: float
    _subject: Subject

    def __init__(self, subject: Subject, func: "function") -> None:
        """Initialize fields from parameters,
           add self as observer to subject."""
        subject.attach(self)
        self._func = func
        self._value = self._func(subject.get_state())
        self._subject = subject

    def get_state(self) -> float:
        """Return state of this object."""
        return self._value

    def update(self) -> None:
        """Change state to reflect updated subject."""
        self._value = self._func(self._subject.get_state())

def main():
    # Create a subject and two different observers.
    subject = Subject()
    observer_1 = Observer(subject, math.factorial)
    observer_2 = Observer(subject, math.sqrt)

    # Update the subject's state and then display state of observers.
    for i in range(10):
        subject.update_state()
        print("Observer 1's state: "
              + str(observer_1.get_state()))
        print("Observer 2's state: " + str(observer_2.get_state()) + "\n")

main()




        
