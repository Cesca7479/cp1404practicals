"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint


def main():
    """ Receive score from user, provide result of score. Also prints result of a random score """
    score = float(input("Enter score: "))
    print(determine_result(score))
    # The following two lines can be reduced to 1,
    # dependent on if the random score needs to be stored and redisplayed.
    # done simply with the following:
    # print(f"Result of random score: {determine_result(randint(0, 100)}")
    random_score = randint(0, 100)
    print(f"Result of random score ({random_score}): {determine_result(random_score)}")


def determine_result(score):
    """ Determine result based off score provided """
    if score < 0 or score > 100:
        return "Invalid Score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"

    # All 'elif's were replaced with 'if' statements, and else was removed as the function will have
    # already returned to main() if any of the previous statements were true.
    # This was suggested by pylint


main()
