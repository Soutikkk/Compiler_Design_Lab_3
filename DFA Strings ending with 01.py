# DFA for binary strings ending with "01"

dfa = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q2', '1': 'q1'},
    'q2': {'0': 'q0', '1': 'q1'}
}

start_state = 'q0'
final_states = ['q2']

string = input("Enter binary string: ")

current_state = start_state

print("\nState Transitions:")

for symbol in string:
    if symbol not in ['0', '1']:
        print("Invalid Input")
        exit()

    print(current_state, "--", symbol, "-->", end=" ")
    current_state = dfa[current_state][symbol]
    print(current_state)

print("\nFinal State:", current_state)

if current_state in final_states:
    print("Result: ACCEPTED")
else:
    print("Result: REJECTED")