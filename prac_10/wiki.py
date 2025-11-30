"""
Program that asks user for an input until they enter a blank line.
Prints details of the wikipedia page for the input requested
"""
import wikipedia


def main():
    """Get input from user and print stuff until they enter a blank line."""
    string = input("Enter page title: ")
    while string != "":
        # print stuff
        try:
            search = wikipedia.page(string, auto_suggest=False)
            print(search.title)
            print(search.summary)
            print(search.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"Page id \"{string}\" does not match any pages. Try another id!")
        string = input("\nEnter page title: ")
    print("Thank you.")


main()
