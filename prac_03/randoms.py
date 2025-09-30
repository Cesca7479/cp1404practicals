"""
Print a random number from 1 to 100, inclusive
"""
# Question 1:
# Smallest number was 5, largest was 20. random.randint is inclusive of bounds

# Question 2:
# Smallest number was 3, largest was 9.
# No, it could not produce a 4. Only generates in range 3 - 10, every 2 numbers.

# Question 3:
# Smallest possible is 2.5, largest is 5.5, depending on rounding

from random import randint

print(randint(1, 100))  # assuming integers
