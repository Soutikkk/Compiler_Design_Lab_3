string = input("Enter binary string: ")

if all(ch in "01" for ch in string):
    if string.startswith("11"):
        print("Result : ACCEPTED")
    else:
        print("Result : REJECTED")
else:
    print("Invalid Input")
