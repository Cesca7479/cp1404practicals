"""
Provide answers to multiple questions regarding the files section
"""

# 1 - Ask user for name, open file called name.txt, write to it.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2 - name.txt file, open file and read the above name, printing a message
in_file = open("name.txt", "r")
name_in_file = in_file.read().strip()
print(f"Hi {name_in_file}!")
in_file.close()

# 3 - open numbers file, read only the first two numbers, add together
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())
    second_number = int(numbers_file.readline())
print(first_number + second_number)

# 4 - prints total for all lines in a file
total = 0
with open("numbers.txt", "r") as file_of_numbers:
    for line in file_of_numbers:
        total += int(line)
print(f"Total: {total}")
