import re

# Token patterns
token_patterns = [
    ('KEYWORD',    r'\b(int|float|if|else|while|for|return)\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('NUMBER',     r'\b\d+(\.\d+)?\b'),
    ('OPERATOR',   r'[+\-*/=<>]'),
    ('DELIMITER',  r'[(),;{}]'),
    ('WHITESPACE', r'\s+'),
]

# Combine all patterns
token_regex = '|'.join(
    f'(?P<{name}>{pattern})'
    for name, pattern in token_patterns
)

def lexical_analyzer(code):
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group()

        # Ignore whitespace
        if token_type != 'WHITESPACE':
            print(f'{token_type:<12} : {token_value}')


# Input source code
code = """
int a = 10;
float b = 20.5;
if (a < b) {
    a = a + 5;
}
"""

print("Tokens:")
lexical_analyzer(code)