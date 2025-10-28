"""
Program that uses the Guitar class
Estimated:  25
Actual:
"""
from prac_06.guitar import Guitar


def main():
    """Collect guitar information, displays information in organised format"""
    guitars = []


def get_information():
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    return Guitar(name, year, cost)
