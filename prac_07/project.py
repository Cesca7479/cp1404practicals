"""
Define Project class that contains information on projects including
project name, start date, priority, estimated cost and completion status.
"""
import datetime


class Project:
    """Contain information on project objects."""

    def __init__(self, name="", start_date=datetime.date.today(), priority=0, cost=0.0, completion=0):
        """Initialise Project attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        """Return attributes in a formatted string."""
        return (f"{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        """Determine an order of projects, by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if a project is complete."""
        return self.completion == 100

    def is_after(self, date):
        """Determine if a project was created after a certain date."""
        return self.start_date >= date

    # Conflicting statement in instructions. Under filter projects by date, it says "display only projects that start
    # AFTER that date."
    # Sample output displays projects that are ON OR AFTER that date
