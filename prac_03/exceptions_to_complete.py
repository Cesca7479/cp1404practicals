"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Do we keep this here even though it won't fail if we try this code?
        # Is it better programing to put it in an else: statement?
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)  # Safe to ignore
