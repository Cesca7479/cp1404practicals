"""
Receive a score, evaluate it and show stars equal to the number of the score
"""

MENU = "(G)et a valid score \n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """ Receive score, show result, print stars """
    score = ""
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


def is_empty(score):
    """ Check if score is still empty. Is used twice """
    if score == "":
        print("Please input a score first")  # I wanted to give feedback to user instead of quitting
        return True  # This feels inefficient
    return False


def print_result(score):
    """ Print result from score """
    if is_empty(score):  # I wasn't sure how else to handle this, without repeating myself more.
        return
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    """ Print number of *'s for the size of score """
    if is_empty(score):
        return
    print("*" * score)


main()
