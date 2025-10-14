"""
Emails
Estimate:   20 minutes
Actual:     15 minutes
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    name = " ".join(email[:email.find("@")].split(".")).title()
    choice = input(f"Is your name {name}? (Y/n) ").upper()
    if choice != "Y" and choice != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")
print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")
