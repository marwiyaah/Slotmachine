MAX_LINE = 3        # global var (unchangeable)

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
        lines = input("How many lines you want to put?: 1-" + str(MAX_LINE) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Please enter a line number between 1 to 3.")
        else:
            print("Please enter a valid line numeber.")

    return lines

get_number_of_lines()
def main():
    balance = deposit()

main()