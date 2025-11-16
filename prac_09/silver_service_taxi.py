"""
Silver Service taxi Class, inherited from Taxi.
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent Silver Service Taxi Class."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise Silver Service Taxi Class."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return formated string."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the Silver Service Taxi Trip."""
        return super().get_fare() + self.flagfall
