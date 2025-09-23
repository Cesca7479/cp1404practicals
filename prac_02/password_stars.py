"""
Collect valid password from user and display password as *'s
"""
MINIMUM_LENGTH = 6
password = input("Password: ")
length = len(password)
while length < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} characters long")
    password = input("Password: ")
    length = len(password)
print("*" * length)
