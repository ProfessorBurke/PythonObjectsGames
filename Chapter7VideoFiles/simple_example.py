"""
    Multiple inheritance example.
"""

from datetime import date

class CalendarItem():
    """Represent one item in a calendar.

       Public methods:  __init__, __str__, activate
    """

    # Annotate object-level fields
    _date: date
    _name: str
    _calendar: "Calendar"

    def __init__(self, item_date: date,
                 name: str, calendar: "Calendar", **kwargs) -> None:
        """Initialize fields from parameters."""
        super().__init__(**kwargs)
        self._date = item_date
        self._name = name
        self._calendar = calendar

    def activate(self) -> None:
        """Take necessary action as item date is now."""
        pass

    def __str__(self) -> str:
        """Return a string version of the calendar item."""
        return (super().__str__() + "\n" + str(self._date) + "\n"
                + self._name + "\n")

class Course():
    
    """A college course.

       Public methods: __init__, get_name, get_description
    """

    # Annotate object-level fields
    _name: str
    _description: str

    def __init__(self, course_name: str, description: str, **kwargs) -> None:
        """Initialize the object from the parameters."""
        super().__init__(**kwargs)
        self._name = course_name
        self._description = description

    def get_course_name(self) -> str:
        """Return the course name."""
        return self._name

    def get_description(self) -> str:
        """Return the course description."""
        return self._description

    def __str__(self) -> str:
        """Return a string version of the course."""
        return (super().__str__() + "\n" + self._name + "\n"
                + self._description)

class Section(CalendarItem, Course):
    """
    """

    # Define object-level fields:
    _professor: str
    _location: str
    _students: list

    def __init__(self, professor: str, location: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self._professor = professor
        self._location = location
        self._students = []

    def register(self, student_name: str) -> None:
        """Register the student for the course."""
        self._students.append(student_name)

    def activate(self) -> None:
        """Tell the student to go to class!"""
        print("Time for class!")
        print("Go to {} for {}.".format(self._location, self.get_course_name()))

    def __str__(self) -> str:
        """Return a string version of the object."""
        return (super().__str__() + "\n" + self._professor + "\n" +
                self._location + "\n" + str(self._students))
    

def main() -> None:
    """Test the classes."""
    item = CalendarItem(date(2023, 1, 1), "Make resolutions", None)
    course = Course("Intro OO Programming",
                    "Learn to program OO systems in Python.")
    #print(item)
    #print(course)

    section = Section(professor = "Maggie",
                      location = "online",
                      item_date = date(2022, 9, 1),
                      course_name = "Intro to OO Programming",
                      name = "Go to class",
                      calendar = None,
                      description = "Learn to program OO systems in Python.")
    #section.activate()
    section.register("Me!")
    print(section)

main()
    
