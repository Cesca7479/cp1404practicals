"""
Define a class that contains information on a guitar
Estimated:   12
Actual:      10
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Store name, year and cost of a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise parameters in a guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted information in a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Determine if a guitar was made before another."""
        return self.year < other.year

    def get_age(self):
        """Determine age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is considered vintage."""
        return self.get_age() >= VINTAGE_AGE
