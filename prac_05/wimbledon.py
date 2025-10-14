"""
Wimbledon
Estimate:  30 minutes
Actual:     minutes
"""
FILENAME = 'wimbledon.csv'


def main():
    lists = read_file(FILENAME)
    champion_to_wins = process_data(lists)


def read_file(filename):
    lists = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            lists.append(in_file.readline().split(","))
    return lists


def process_data(lists):
    champion_to_wins = {}
    countries_of_champions = []
    for part in lists:
        champion_to_wins[part[2]] = champion_to_wins.get(part[2], 0) + 1
        countries_of_champions.append(part[1])
    return champion_to_wins, sorted(set(countries_of_champions))


def display_information():
    pass


main()
