"""
Ask user for a number of "quick picks", generate that many lines of output
"""

from random import randint

MINIMUM = 1
MAXIMUM = 45

# Question asks for 'program', no mention of functions like what's shown in the answers.
number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_picks = []
    for k in range(6):
        number = randint(MINIMUM, MAXIMUM)
        while number in quick_picks:
            number = randint(MINIMUM, MAXIMUM)
        quick_picks.append(number)
    print(" ".join(f"{number:2}" for number in sorted(quick_picks)))
