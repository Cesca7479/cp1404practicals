"""
Unreliable car test.
"""

from unreliable_car import UnreliableCar

ITERATIONS = 100000


def main():
    """Test Unreliable Car Class."""
    cars = [UnreliableCar("Bad Car", ITERATIONS, 30), UnreliableCar("Better Car", ITERATIONS, 90)]
    for car in cars:
        for i in range(ITERATIONS):
            car.drive(1)
        car_reliability = 100 * (ITERATIONS - car.fuel) / ITERATIONS
        print(f"{car.name} drove {car_reliability}% of the time, reliability was {car.reliability}%")


main()
