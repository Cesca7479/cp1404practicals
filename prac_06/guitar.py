"""
Class that contains information on a guitar
Estimated:   12
Actual:      10
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Stores name, year and cost of a guitar"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialises parameters in a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns formatted information in a string"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Boolean for age of guitar being over 50"""
        return self.get_age() >= VINTAGE_AGE
