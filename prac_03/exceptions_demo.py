"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# 1. ValueError occurs when anything but a number is inputted
# 2. ZeroDivisionError occurs when the denominator is equal to 0.
# 3. Yes - LBYL. Only run the division if the denominator is not 0, or force the
#       user to enter a non-zero denominator value.


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
except ValueError:
    print("Numerator and denominator must be valid numbers!")
else:
    # I acknowledge that this can be turned into a while loop that forces the user to input
    # a correct number for the denominator. However, the question was ambiguous, so I was not sure
    # Note, this was put here as it will run only if the ValueError doesn't occur. It does not need
    # to be within the try statement as no error can occur here.
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by 0")
print("Finished.")

# code to put instead of the above if statement:
# while denominator == 0:
#     print("Please enter a non-zero denominator")
#     denominator = int(input("Enter the denominator: "))

# Use this code inside the try statement, and remove the if statement, by just putting the division inside the else
