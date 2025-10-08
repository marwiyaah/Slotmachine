import random

MAX_LINE = 3        # global var (unchangeable)
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# dictionary
symbol_count = {
    "A" : 2,        # A is there 2 times (symbols : symbol_count)
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def get_slotmachine_wheel(rows, cols, symbols):
    all_symbols = [] # list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):       # _ is an unknown var in python. when you dont care about the number or iteration value, just need to loop through, this could be used
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]        # copy of all_symbols list
        for _ in range(rows):
            value = random.choice(current_symbols)      # select a random symbol
            current_symbols.remove(value)               # remove the selected symbol from the list. so if a is selected and there are 2 As then 1 A will be removed
            column.append(value)                        # add the selected symbol to the column (row actually)

        columns.append(column)

    return columns

def print_slotmachine(columns):
    for row in range(len(columns[0])):          # assuming at least 1 row there
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")       # end = newline char
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Please give an amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines you want to put?: (1-" + str(MAX_LINE) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Please enter a line number between 1 to 3.")
        else:
            print("Please enter a valid line number.")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line?: $" )
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")     # f string
        else:
            print("Please enter a valid number.")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to play this amount. Current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")

    slots = get_slotmachine_wheel(ROWS, COLS, symbol_count)
    print_slotmachine(slots)

main()