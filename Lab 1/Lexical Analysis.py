import re

code = input("Enter a statement:\n")

keywords = {
    "if", "else", "while", "for", "int",
    "float", "char", "return", "void"
}

operators = {
    "+", "-", "*", "/", "=", "==",
    "<", ">", "<=", ">=", "!="
}

delimiters = {
    "(", ")", "{", "}", ";", ","
}

tokens = re.findall(r"[A-Za-z_]\w*|\d+|==|<=|>=|!=|[-+*/=(){};,<>]", code)

print("\nTOKEN\t\tTYPE")

for token in tokens:

    if token in keywords:
        t = "Keyword"

    elif token in operators:
        t = "Operator"

    elif token in delimiters:
        t = "Delimiter"

    elif token.isdigit():
        t = "Constant"

    else:
        t = "Identifier"

    print(f"{token}\t\t{t}")
