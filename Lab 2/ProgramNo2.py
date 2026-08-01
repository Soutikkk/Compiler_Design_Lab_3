# Python Program to Check Operators Between Operands

expression = input("Enter an expression: ").replace(" ", "")

operators = ['+', '-', '*', '/', '%']

valid = True

for i, ch in enumerate(expression):
    if ch in operators:
        if i == 0 or i == len(expression) - 1:
            valid = False
            break
        elif not (expression[i - 1].isalnum() and expression[i + 1].isalnum()):
            valid = False
            break

if valid:
    print("Valid expression: Operators are correctly placed between operands.")
else:
    print("Invalid expression: Operator placement is incorrect.")