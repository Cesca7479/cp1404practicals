"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

COLOUR_TO_HEX = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "Amber": "#ffb00", "Amethyst": "#9966cc",
                 "Aqua": "#00ffff", "BarnRed": "#7c0a02", "Black": "#000000", "Bole": "#79443b", "BrightUbe": "#d19fe8",
                 "Brown": "#a52a2a"}
COLOUR_TO_HEX_LOWER = {colour.lower(): hex_code for colour, hex_code in COLOUR_TO_HEX.items()}

maximum_colour_length = max(len(colour) for colour in COLOUR_TO_HEX.keys())
for colour, hex_code in COLOUR_TO_HEX.items():
    print(f"{colour:{maximum_colour_length}} is {hex_code}")

state_code = input("Enter a colour: ").lower()
while state_code != "":
    try:
        print(state_code, "is", COLOUR_TO_HEX_LOWER[state_code])
    except KeyError:
        print("Invalid colour")
    state_code = input("Enter a colour: ").lower()
