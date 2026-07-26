symbol_table = {}

def insert_symbol():
    name = input("Enter symbol name: ")
    dtype = input("Enter data type: ")
    address = input("Enter memory address: ")

    symbol_table[name] = {
        "Type": dtype,
        "Address": address
    }

    print("Symbol inserted successfully.\n")


def search_symbol():
    name = input("Enter symbol to search: ")

    if name in symbol_table:
        print("Symbol Found:")
        print(symbol_table[name])
    else:
        print("Symbol not found.")


def display_table():
    print("\n------ SYMBOL TABLE ------")
    print("{:<15} {:<15} {:<15}".format("Symbol", "Type", "Address"))

    for key, value in symbol_table.items():
        print("{:<15} {:<15} {:<15}".format(
            key,
            value["Type"],
            value["Address"]
        ))

    print()


while True:

    print("\n===== SYMBOL TABLE MENU =====")
    print("1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            insert_symbol()

        elif choice == 2:
            search_symbol()

        elif choice == 3:
            display_table()

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")
