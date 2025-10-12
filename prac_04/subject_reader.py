"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Call functions to load subject details and print them"""
    subjects = load_subject_details(FILENAME)
    print_subject_details(subjects)


def load_subject_details(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subjects = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subjects.append(parts)
    input_file.close()
    return subjects


def print_subject_details(subjects):
    """Print data provided in format: subject, lecturer, number of students"""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))
        # star unpacks each list, useful for code adjustability


main()
