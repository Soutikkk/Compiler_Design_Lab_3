import re

keywords = {
    "int", "float", "char", "double", "if", "else", "while",
    "for", "return", "break", "continue", "void", "main",
    "switch", "case", "default", "do", "struct", "typedef",
    "const", "unsigned", "long", "short", "signed"
}

operators = {
    "+", "-", "*", "/", "%", "=", "==", "!=", "<", ">",
    "<=", ">=", "&&", "||", "++", "--"
}

delimiters = {
    ";", ",", "(", ")", "{", "}", "[", "]"
}

special_symbols = {
    "#", "@", "$", "&"
}

print("Enter C Program (Type END on a new line to finish):")

code = ""

while True:
    line = input()
    if line == "END":
        break
    code += line + "\n"

print("\n------ C PROGRAM ------")
print(code)

token_pattern = r'''
==|!=|<=|>=|\+\+|--|\|\||&&|
[A-Za-z_][A-Za-z0-9_]*|
\d+\.\d+|\d+|
[+\-*/%=<>]|
[;,(){}\[\]]|
[#@$&]
'''

tokens = re.findall(token_pattern, code, re.VERBOSE)

keyword_count = 0
identifier_count = 0
operator_count = 0
delimiter_count = 0
constant_count = 0
special_count = 0

for token in tokens:

    if token in keywords:
        keyword_count += 1

    elif token in operators:
        operator_count += 1

    elif token in delimiters:
        delimiter_count += 1

    elif token in special_symbols:
        special_count += 1

    elif re.fullmatch(r'\d+\.\d+|\d+', token):
        constant_count += 1

    elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
        identifier_count += 1

print("\n========== TOKEN COUNT ==========")
print("+-------------------+-------+")
print("| Token Type        | Count |")
print("+-------------------+-------+")
print(f"| Keywords          | {keyword_count:^5} |")
print(f"| Identifiers       | {identifier_count:^5} |")
print(f"| Operators         | {operator_count:^5} |")
print(f"| Delimiters        | {delimiter_count:^5} |")
print(f"| Constants         | {constant_count:^5} |")
print(f"| Special Symbols   | {special_count:^5} |")
print("+-------------------+-------+")