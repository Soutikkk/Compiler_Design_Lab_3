# Python Program to Check Valid Operators

expression = input("Enter an expression: ")

# List of valid operators
valid_operators = {
    "+", "-", "*", "/", "%", "**", "//",
    "=", "==", "!=", ">", "<", ">=", "<=",
    "+=", "-=", "*=", "/=", "%=",
    "&", "|", "^", "~", "<<", ">>",
    "and", "or", "not"
}

# Operators to check (longest first)
operators = [
    "**", "//", "==", "!=", ">=", "<=", "<<", ">>",
    "+=", "-=", "*=", "/=", "%=",
    "+", "-", "*", "/", "%", "=",
    ">", "<", "&", "|", "^", "~"
]

found = []

for op in operators:
    if op in expression:
        found.append(op)

print("\nOperators found in the expression:")
if found:
    for op in found:
        if op in valid_operators:
            print(op, "-> Valid")
        else:
            print(op, "-> Invalid")
else:
    print("No operators found.")