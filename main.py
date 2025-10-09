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

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings = values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


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

def spin(balance):
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
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"You won ${winnings}.")
    print(f"You won on lines:",*winning_lines)  # *splat/unpack operator = passes every single line from the winning lines list. so if the user wins on line 1 and 2 the print statement will show "You won on line 1,2
    return winnings - total_bet        # this will tell us how much they won/lost in this game

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to continue... (q to quit) : ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with ${balance}.")

main()