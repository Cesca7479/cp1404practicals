"""
Run through a menu that allows a user to load, display, filter, add and update projects.
Estimated: 3 hrs
Actual:    2hr, 44 min
"""
import datetime
from operator import attrgetter

from prac_07.project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
DEFAULT_FILENAME = "projects.txt"
LOWEST_PRIORITY = 10
INPUT_REQUIRED_PROMPTS = ("Project choice: ", "Priority: ", "Percent complete: ")


def main():
    """Load default projects file, cycle through a menu, provide option to save file upon completion."""
    print("Welcome to Pythonic Project Management")
    projects = load_file(DEFAULT_FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = get_valid_string("Enter a file to load projects from: ")
            # new_projects = load_file(filename)
            # projects.append(new_projects)  # Do you want to keep the old projects, or just use new ones?
            projects = load_file(filename)
        elif choice == "S":
            filename = get_valid_string("Enter a file to save projects to: ")
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
    # Googled how to stop .strip(",") from deleting white space after comma, found replace method
    decision = list(input(f"Would you like to save to {DEFAULT_FILENAME}? ").replace(",", "").upper().split())
    while "NO" not in decision and "YES" not in decision:
        print("Sorry, I didn't understand. Try using yes or no.")
        decision = list(input(f"Would you like to save to {DEFAULT_FILENAME}? ").replace(",", "").upper().split())
    if "YES" in decision:
        save_projects(DEFAULT_FILENAME, projects)
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
    print(f"{len(projects)} projects saved to {filename}")


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
    date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    projects_after_date = [project for project in sorted(projects, key=attrgetter('start_date')) if
                           project.is_after(date)]
    for project in projects_after_date:
        print(project)
    if not projects_after_date:
        print(f"There are no projects that started after {date.strftime("%d/%m/%Y")}")


def get_new_project():
    """Add a new project to the list."""
    print("Let's add a new project")
    name = get_valid_string("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_input("Priority: ", LOWEST_PRIORITY, 1)
    cost = get_valid_float("Cost estimate: $")
    completion = get_valid_input("Percent complete: ", 100, 0)
    return Project(name, start_date, priority, cost, completion)


def get_valid_string(prompt):
    """Get a string from user, mustn't be blank."""
    string = input(prompt)
    while string == "":
        string = input(prompt)
    return string


def get_valid_date(prompt):
    valid_date = False
    while not valid_date:
        date_string = input(prompt)
        try:
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            valid_date = True
        except ValueError:
            print("Invalid date")
    return date


def get_valid_float(string):
    """Get a valid float."""
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
    choice = get_valid_input("Project choice: ", len(projects) - 1, 0)
    print(projects[choice])
    new_percentage = get_valid_input("New Percentage: ", 100, 0)
    new_priority = get_valid_input("New Priority: ", LOWEST_PRIORITY, 1)
    if new_percentage:
        projects[choice].completion = new_percentage
    if new_priority:
        projects[choice].priority = new_priority


def get_valid_input(string, maximum, minimum):
    """Get a valid input from the user, which must be less than the maximum or blank."""
    valid_input = False
    while not valid_input:
        input_string = input(string)
        if input_string == "" and string not in INPUT_REQUIRED_PROMPTS:
            return None
        else:
            try:
                number = int(input_string)
                if number < minimum or number > maximum:
                    print(f"Number must be at least {minimum} and smaller than or equal to {maximum}")
                else:
                    valid_input = True
            except ValueError:
                print("Invalid Number")
    return number  # Nesting is REALLY terrible here.


main()
