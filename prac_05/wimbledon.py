"""
Wimbledon
Estimate:  30 minutes
Actual:     minutes
"""
FILENAME = 'wimbledon.csv'


def main():
    print(read_file(FILENAME))


def read_file(filename):
    lists = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            lists.append(in_file.readline().split(","))
    return lists


def process_data():
    pass


def display_information():
    pass


main()
