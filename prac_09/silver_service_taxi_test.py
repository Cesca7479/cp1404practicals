"""
Test Silver Service Taxi Class.
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the Silver Service Taxi Class."""
    hummer_taxi = SilverServiceTaxi("Hummer", 200, 4)
    assert str(hummer_taxi) == "Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50"
    silver_taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    silver_taxi.drive(18)
    assert silver_taxi.get_fare() == 48.80


main()
