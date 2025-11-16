"""
Test Taxi Class.
"""
from taxi import Taxi


def main():
    """Test Taxi."""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(f"{my_taxi}, current fair: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, current fair: ${my_taxi.get_fare():.2f}")


main()
