"""
Receive a score, evaluate it and show stars equal to the number of the score
"""

MENU = "(G)et a valid score \n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """ Receive score, show result, print stars """
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Bad input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """ Get a valid score from user """
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def print_result(score):
    """ Print result from score """
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    """ Print number of *'s for the size of score """
    print("*" * score)


main()
