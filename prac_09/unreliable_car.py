"""
Create Unreliable Car Class, derived from Car.
"""

from car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an Unreliable Car Object."""

    def __init__(self, name, fuel, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with car unreliability."""
        return f"{super().__str__()}, reliability: {self.reliability}%"

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven

