"""
Run through a menu that allows a user to load, display, filter, add and update projects
Estimated: 3 hrs
Actual:
"""

import datetime

from prac_07.project import Project

MENU = ("- (L)oad projects"
        "- (S)ave projects"
        "- (D)isplay projects"
        "- (F)ilter projects"
        "- (A)dd new project"
        "- (U)pdate project"
        "- (Q)uit")
DEFAULT_FILENAME = "projects.txt"


def main():
    """Load default projects file, cycle through a menu, provide option to save file upon completion."""
    projects = load_file(DEFAULT_FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")


def load_file(filename):
    """Load contents of file and store Projects in a list"""
    projects = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost = float(parts[3])
            completion = float(parts[4])
            project = Project(parts[0], start_date, priority, cost, completion)
            projects.append(project)
    return projects


main()
