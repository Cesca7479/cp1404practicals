"""
Collect valid password from user and display password as *'s
"""
MINIMUM_LENGTH = 6


def main():
    """ Receive valid password from user, print to screen """
    password = get_password()
    print_password(password)


def print_password(password: str):
    """ Print password in the form of '*' """
    print("*" * len(password))


def get_password() -> str:
    """ Collect and validate the password provided by user """
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long")
        password = input("Password: ")
    return password


main()
