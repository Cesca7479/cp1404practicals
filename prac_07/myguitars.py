"""
Read guitars.csv and use Guitar class to manipulate data.
"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
CURRENT_YEAR = 2025


def main():
    """Load guitars from a file, sort and print to screen."""
    guitars = sorted(load_guitars(FILENAME))
    display_guitars(guitars)
    guitars = get_guitars(guitars)
    display_guitars(guitars)
    save_guitars(guitars, FILENAME)


def get_guitars(guitars):
    """Get new guitars from user"""
    name = input("Name: ")
    while name != "":
        year = get_valid_year()
        cost = get_valid_cost()
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")
    return sorted(guitars)


def get_valid_year():
    """Get a valid year."""
    is_valid = False
    while not is_valid:
        try:
            year = int(input("Year: "))
            if year > CURRENT_YEAR or year <= 0:
                print("Invalid year")
            else:
                is_valid = True
        except ValueError:
            print("Invalid year")
    return year


def get_valid_cost():
    """Get a valid cost."""
    is_valid = False
    while not is_valid:
        try:
            cost = float(input("Cost: "))
            if cost < 0:
                print("Cost must be positive")
            else:
                is_valid = True
        except ValueError:
            print("Invalid Cost")
    return cost


def load_guitars(filename):
    """Load guitars from a file, store in guitars list."""
    guitars = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(parts[0], year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display guitars neatly."""
    longest_name_length = max(len(guitar.name) for guitar in guitars)
    longest_cost_length = max(len(str(f"{guitar.cost:,.2f}")) for guitar in guitars)
    for guitar in guitars:
        print(f"{guitar.name:{longest_name_length}} ({guitar.year}) : ${guitar.cost:{longest_cost_length},.2f}")


def save_guitars(guitars, filename):
    """Save guitars to file in csv format"""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
