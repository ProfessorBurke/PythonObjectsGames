"""A polymorphism example from the course software."""
from datetime import date


class Assignment():
    """A course assignment.

       Public methods:  __init__, get_grade
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

    def get_grade(self) -> int:
        """Return the grade for this assignment."""
        return self._grade


class Essay(Assignment):
    """An essay type of assignment.

       Public method: __init__
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
        super().__init__(year_due, month_due, day_due)
        self._prompt = prompt
        self._response = None


class Quiz(Assignment):
    """A quiz type of assignment.

       Public methods:  __init__, get_grade
    """

    # Annotate object-level fields
    _questions: list
    _answers: list
    _response: list

    def __init__(self,
                 year_due: int,
                 month_due: int,
                 day_due: int,
                 questions: list,
                 answers: list) -> None:
        """Initialize the essay from parameters."""
        super().__init__(year_due, month_due, day_due)
        self._questions = questions
        self._answers = answers
        # Hard-coded response for testing purposes.
        self._response = [True, False]

    def get_grade(self) -> int:
        """Return the grade for this assignment."""
        # Initialize and annotate variables
        total: int = 0
        i: int

        # Iterate through answer key and answers and count
        # correct answers.
        for i in range(len(self._answers)):
            if self._answers[i] == self._response[i]:
                total += 1
                
        return total / len(self._answers) * 100
    
def main() -> None:
    """Create assignments and get grades."""
    # Initialize and annotate assignment list
    assignments: list[Assignment] = []

    # Create two assignments.
    assignments.append(Essay(2019, 11, 30,
                            "Explain the \"isa\" relationship."))
    assignments.append(Quiz(2019, 11, 30,
                            ["Guido van Rossum authored Python",
                             "UML diagrams OO systems"],
                            [True, True]))
    
    # Send the get_grade message to the assignments.
    for assignment in assignments:
        print(assignment.get_grade())

main()
    
