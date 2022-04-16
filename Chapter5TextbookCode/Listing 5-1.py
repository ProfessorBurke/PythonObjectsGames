"""An inheritance example from the course software."""
from datetime import date


class Assignment():
    """A course assignment.

       Public methods:  __init__, assign_grade,
                        __str__
    """

    # Annotate object-level fields
    _feedback: str
    _grade: int
    _due_date: date

    def __init__(self,
                 year_due: int,
                 month_due: int,
                 day_due: int) -> None:
        """Initialize an assignment from parameters."""
        self._feedback = None
        self._grade = 0
        self._due_date = date(year_due, month_due, day_due)


    def assign_grade(self, grade: int) -> None:
        """Assign a grade to this assignment."""
        self._grade = grade

    def __str__(self) -> str:
        """Convert assignment to a string."""
        return "{:12s}{}\n{:12s}{}\n{:12s}{}".format(
            "Grade:", self._grade,"Feedback:", self._feedback,
            "Due date:", self._due_date)

class Essay(Assignment):
    """An essay type of assignment.

       Public methods:  __init__, __str__
    """

    # Annotate object-level fields
    _prompt: str
    _response: str

    def __init__(self, 
                 year_due: int,
                 month_due: int,
                 day_due: int,
                 prompt: str) -> None:
        """Initialize the essay from parameters."""
        super().__init__(**kwargs)
        self._prompt = prompt
        self._response = None

    def __str__(self) -> str:
        """Convert essay to a string."""
        return (super().__str__() +
                "\n\n{:12s}{}\n{:12s}{}".format(
                    "Prompt:", self._prompt, "Response:",
                    self._response))

def main() -> None:
    """Create an essay and print."""
    # Annotate variable
    essay: Essay

    # Create an Essay Assignment, set grade, and print.
    essay = Essay(year_due = 2019, month_due = 11, day_due = 30,
                  prompt = "Explain the \"isa\" relationship.")
    essay.assign_grade(100)
    print(essay)

main()
    
