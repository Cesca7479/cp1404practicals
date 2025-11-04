"""
Create some languages using the ProgrammingLanguage class, print out details
Estimate:   5
Actual:     2
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]

print("The dynamically typed languages are: ")
[print(language.name) for language in languages if language.is_dynamic()]
