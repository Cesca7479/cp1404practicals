"""
Wimbledon
Estimate:  30 minutes
Actual:    35 minutes
"""
FILENAME = 'wimbledon.csv'


def main():
    matches = read_file(FILENAME)
    champion_to_wins, countries_of_champions = process_data(matches)
    display_information(champion_to_wins, countries_of_champions)


def read_file(filename):
    matches = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            matches.append(line.split(","))
    return matches


def process_data(matches):
    champion_to_wins = {}
    countries_of_champions = []
    for match in matches:
        champion_to_wins[match[2]] = champion_to_wins.get(match[2], 0) + 1
        countries_of_champions.append(match[1])
    return champion_to_wins, sorted(set(countries_of_champions))


def display_information(champion_to_wins, countries_of_champions):
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(champion, wins)
    print()
    print(f"These {len(countries_of_champions)} have won Wimbledon:")
    print(", ".join(countries_of_champions))


main()
