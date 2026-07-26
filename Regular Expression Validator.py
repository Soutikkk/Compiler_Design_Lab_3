import re

pattern = r"^a*b+$"

string = input("Enter input string: ")

if re.fullmatch(pattern, string):
    print("\nResult : VALID STRING")
    print("The string matches the Regular Expression.")
else:
    print("\nResult : INVALID STRING")
    print("The string does not match the Regular Expression.")
