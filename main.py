MAX_LINE = 3        # global var (unchangeable)
MAX_BET = 100
MIN_BET = 1

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


main()