"""
Store information about languages in a class
Estimate:   15
Actual:     10
"""


class ProgrammingLanguage:
    """Contains typing, reflection and year made for a programming language"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialises parameters for a language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a string of the information"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns Boolean on if language is dynamic"""
        return self.typing == "Dynamic"
