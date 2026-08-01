# Python Program to Remove Extra White Spaces

string = input("Enter a string: ")
result = ""
i = 0

while i < len(string):
    if string[i] != ' ' and string[i] != '\t':
        result += string[i]
    else:
        result += ' '
        while i < len(string) and (string[i] == ' ' or string[i] == '\t'):
            i += 1
        i -= 1
    i += 1

print("\nString after removing extra white spaces:")
print(result)