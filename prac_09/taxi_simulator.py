"""
Use Taxi and SilverServiceTaxi Classes to run a taxi simulator program
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d(rive"


def main():
    """Run Taxi Simulator."""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill}")
        print(MENU)
        choice = input(">>> ").lower()


def choose_taxi(taxis):
    """Get taxi choice from user."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    choice = int(input("Choose taxi: "))
    if choice < 0 or choice >= len(taxis):
        print("Invalid taxi choice")
        return None
    return taxis[choice]


def drive_taxi(current_taxi):
    """Drive chosen taxi."""
    if not current_taxi:
        print("You need to choose a taxi before you can drive")
    else:
        distance = int(input("Drive how far? "))
        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fair()}")
    return current_taxi.get_fare()


main()
