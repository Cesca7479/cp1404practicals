"""
Run through a menu that allows a user to load, display, filter, add and update projects.
Estimated: 3 hrs
Actual:    1 hr, 23 min
"""
import datetime
from operator import attrgetter

from prac_07.project import Project

MENU = ("""- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit""")
DEFAULT_FILENAME = "projects.txt"
LOWEST_PRIORITY = 10


def main():
    """Load default projects file, cycle through a menu, provide option to save file upon completion."""
    print("Welcome to Pythonic Project Management")
    projects = load_file(DEFAULT_FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter a file to load projects from: ")
            # new_projects = load_file(filename)
            # projects.append(new_projects)  # Do you want to keep the old projects, or just use new ones?
            projects = load_file(filename)
        elif choice == "S":
            filename = input("Enter a file to save projects to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            new_project = get_new_project()
            projects.append(new_project)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    decision = list(input(f"Would you like to save to {DEFAULT_FILENAME}? ").upper().split())
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
    return projects


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
    incomplete_projects = [project for project in sorted(projects) if not project.is_complete()]
    completed_projects = [project for project in sorted(projects) if project.is_complete()]
    if incomplete_projects:
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")
    if completed_projects:
        print("Completed projects:")
        for project in completed_projects:
            print(f"  {project}")  # I don't like the nesting here. Can I simplify this?


def filter_projects(projects):
    """Filter projects to display only those after a certain date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    projects_after_date = [project for project in sorted(projects, key=attrgetter('start_date')) if
                           project.is_after(date)]
    for project in projects_after_date:
        print(project)
    if not projects_after_date:
        print(f"There are no projects that started after {date.strftime("%d/%m/%Y")}")


def get_new_project():
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = get_valid_input("Priority: ", LOWEST_PRIORITY)
    cost = get_valid_float("Cost estimate: $")
    completion = get_valid_input("Percent complete: ", 100)
    return Project(name, start_date, priority, cost, completion)


def get_valid_float(string):
    valid_input = False
    while not valid_input:
        try:
            number = float(input(string))
            if number < 0:
                print("Number must be positive")
            else:
                valid_input = True
        except ValueError:
            print("Invalid Number")
    return number


def update_project(projects):
    """Update a project's completion level."""
    for i, project in enumerate(projects):
        print(i, project)
    choice = get_valid_input("Project choice: ", len(projects) - 1)
    print(projects[choice])
    new_percentage = get_valid_input("New Percentage: ", 100)
    new_priority = get_valid_input("New Priority: ", LOWEST_PRIORITY)
    if new_percentage:
        projects[choice].completion = new_percentage
    if new_priority:
        projects[choice].priority = new_priority


def get_valid_input(string, maximum):
    """Get a valid input from the user, which must be less than the maximum or blank"""
    valid_input = False
    while not valid_input:
        input_string = input(string)
        if input_string == "" and string != "Project choice: " and string != "Priority: " and string != "Percent complete: ":
            return None
        else:
            try:
                number = int(input_string)
                if number < 0 or number > maximum:
                    print(f"Number must be larger than 0 and smaller than {maximum}")
                else:
                    valid_input = True
            except ValueError:
                print("Invalid Number")
    return number  # Nesting is REALLY terrible here.


main()
