"""
Program that uses the Guitar class
Estimated:  25
Actual:     29
"""
from prac_06.guitar import Guitar


def main():
    """Collect guitar information, displays information in organised format"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    maximum_guitar_length = max((len(guitar.name)) for guitar in guitars)
    maximum_cost_length = max((len(str(guitar.cost))) for guitar in guitars)
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{maximum_guitar_length}} ({guitar.year}), "
              f"worth $ {guitar.cost:{maximum_cost_length + 2},.2f} {vintage}")


main()
