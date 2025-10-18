"""
Emails
Estimate:   20 minutes
Actual:     15 minutes
"""


def main():
    """Ask the user for their email, confirm their name, print list of emails and names collected"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        choice = input(f"Is your name {name}? (Y/n) ").upper()
        if choice != "Y" and choice != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email: str) -> str:
    """Extract a user's name from their email, return name"""
    name = " ".join(email[:email.find("@")].split(".")).title()
    return name


main()
