"""
Read guitars.csv and use Guitar class to manipulate data.
"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitars from a file, sort and print to screen."""
    guitars = sorted(load_guitars())
    display_guitars(guitars)


def load_guitars():
    """Load guitars from a file, store in guitars list."""
    guitars = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
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


main()
