import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

INVALID_NUMBER_ERROR = "Please enter a valid number.\n"

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
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for index, column in enumerate(columns):
            if index != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def get_number_of_lines():
    while True:
        try:
            number_of_lines = int(input(f"Enter the number of lines to bet on (1-{MAX_LINES}): "))
        except ValueError:
            print(INVALID_NUMBER_ERROR)
            continue

        if number_of_lines < 1 or number_of_lines > MAX_LINES:
            print(f"Please enter a number between 1 and {MAX_LINES}.\n")
            continue

        return number_of_lines

def deposit():
    while True:
        try:
            amount = float(input("Enter amount to be Deposited: "))
        except ValueError:
            print(INVALID_NUMBER_ERROR)
            continue
        
        if amount <= 0:
            print("Please enter a number more than 0.\n")
            continue
            
        return amount
    
def get_bet():
    while True:
        try:
            bet = float(input(f"Enter bet amount ({MIN_BET}-{MAX_BET}): "))
        except ValueError:
            print(INVALID_NUMBER_ERROR)
            continue

        if bet < MIN_BET or bet > MAX_BET:
            print(f"Please enter a number between {MIN_BET} and {MAX_BET}.\n")
            continue

        return bet
            
def play_slot_machine(balance: float):
    if balance <= 0:
        print("You do not have enough balance to play.")
        print_current_balance(balance)
        return balance
    
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
        
    if total_bet > balance:
        print(f"You do not have enough balance to bet {total_bet:.2f}.")
        print_current_balance(balance)
        return balance
    
    print(f"You are betting {bet:.2f} on {lines} lines. Total bet is equal to: {total_bet:.2f}")
        
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    balance += winnings - total_bet
    
    if winnings == 0:
        print(f"You lost {total_bet:.2f}")
    else:
        print(f"You won {winnings:.2f}")
        print("You won on lines:", *winning_lines)
    
    print_current_balance(balance)
    return balance

def print_current_balance(balance: float):
    print(f"Your current balance is: {balance:.2f}")

def main():
    balance = 0
    while True:
        print("\n1. Play Slot Machine\n2. Deposit\n3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            balance = play_slot_machine(balance)
        elif choice == '2':
            balance += deposit()
            print_current_balance(balance)
        elif choice == '3':
            print("Thank you goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()