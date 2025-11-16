"""
Unreliable car test.
"""

from unreliable_car import UnreliableCar

ITERATIONS = 1000000


def main():
    bad_car = UnreliableCar("Bad Car", ITERATIONS, 30)
    for i in range(ITERATIONS):
        bad_car.drive(1)
    car_accuracy = 100*(ITERATIONS - bad_car.fuel)/ITERATIONS
    print(f"Car drove {car_accuracy}% of the time")


main()
