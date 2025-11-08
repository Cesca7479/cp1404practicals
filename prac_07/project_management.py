"""
Run through a menu that allows a user to load, display, filter, add and update projects.
Estimated: 3 hrs
Actual:    1 hr, 23 min
"""
# Do I sort each time, or only when I display or save?
import datetime

from prac_07.project import Project

MENU = ("""- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects
- (A)dd new project
- (U)pdate project
- (Q)uit")""")
DEFAULT_FILENAME = "projects.txt"


# TODO: Complete all functions

def main():
    """Load default projects file, cycle through a menu, provide option to save file upon completion."""
    projects = load_file(DEFAULT_FILENAME)
    print("Welcome to Pythonic Project Management")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter a file to load projects from: ")
            new_projects = load_file(filename)
            projects.append(new_projects)
            projects.sort()
        elif choice == "S":
            filename = input("Enter a file to save projects to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)  # use display function here too
        elif choice == "A":
            add_project()
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    decision = list(input(f"Would you like to save to {DEFAULT_FILENAME} ").upper().split())
    if "YES" in decision:
        save_projects(DEFAULT_FILENAME, projects)
        print(f"Projects saved to {DEFAULT_FILENAME}")
    print("Thank you for using custom-built project management software.")


def load_file(filename):
    """Load contents of file and store Projects in a list."""
    projects = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost = float(parts[3])
            completion = int(parts[4])
            project = Project(parts[0], start_date, priority, cost, completion)
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return sorted(projects)


def save_projects(filename, projects):  # filename
    """Save projects to a chosen file."""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost}\t"
                f"{project.completion}", file=out_file)


def display_projects(projects):
    """Display projects, sorted and in categories of completion status."""
    for project in projects:
        print(f"  {project}")


def filter_projects(projects):  # Do this or combine with display?
    """Filter projects to display only those after a certain date."""
    pass  # Can adjust display to pass in a date, but let date be earliest date of a project for just displaying


# On second thought, no - print looks different


def add_project():
    """Add a new project to the list."""
    pass


def update_project(projects):
    """Update a project's completion level."""
    pass


main()
