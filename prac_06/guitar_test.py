"""
Used to test the guitar class
Estimated:   5
Actual:      7
"""
from prac_06.guitar import Guitar

# CURRENT_YEAR = 2025
# VINTAGE_AGE = 50

guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40),
           Guitar("Another Guitar", 2013, 65765.21)]

# I don't think the following counts as printing literals?
# [print(f"{guitar.name} get_age() - Expected {CURRENT_YEAR - guitar.year}. Got {guitar.get_age()}") for guitar in
#  guitars]
# [print(
#     f"{guitar.name} is_vintage() - Expected {(CURRENT_YEAR - guitar.year) >= VINTAGE_AGE}. Got {guitar.is_vintage()}")
#  for guitar in guitars]

print(f"{guitars[0].name} get_age() - Expected {103}. Got {guitars[0].get_age()}")
print(f"{guitars[1].name} get_age() - Expected {12}. Got {guitars[1].get_age()}")
print(f"{guitars[0].name} is_vintage() - Expected {True}. Got {guitars[0].is_vintage()}")
print(f"{guitars[1].name} is_vintage() - Expected {False}. Got {guitars[1].is_vintage()}")
