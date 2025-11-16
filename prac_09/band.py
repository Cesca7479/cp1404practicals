"""
Band Class.
"""


class Band:
    """Represent Band Object."""

    def __init__(self, name):
        """Initialise Band Object with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return Band name and musicians in the band."""
        return f"{self.name} ({self.musicians})"

    def add(self, musician):
        """Add Musician to the Band."""
        return self.musicians.append(musician)

    def play(self):
        """Return a string stating the musicians who are playing in the band."""
        if not self.musicians:
            return "There are no musicians!"
        return "\n".join(musician.play() for musician in self.musicians)
