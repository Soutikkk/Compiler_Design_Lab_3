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

keyword_count = 0
operator_count = 0
delimiter_count = 0
identifier_count = 0
constant_count = 0

print("\nTOKEN\t\tTYPE")

for token in tokens:

    if token in keywords:
        keyword_count += 1
        token_type = "Keyword"

    elif token in operators:
        operator_count += 1
        token_type = "Operator"

    elif token in delimiters:
        delimiter_count += 1
        token_type = "Delimiter"

    elif token.isdigit():
        constant_count += 1
        token_type = "Constant"

    else:
        identifier_count += 1
        token_type = "Identifier"

    print(f"{token}\t\t{token_type}")

print("\n--------- TOKEN COUNT ---------")
print("Keywords   :", keyword_count)
print("Identifiers:", identifier_count)
print("Operators  :", operator_count)
print("Delimiters :", delimiter_count)
print("Constants  :", constant_count)
print("Total Tokens:", len(tokens))