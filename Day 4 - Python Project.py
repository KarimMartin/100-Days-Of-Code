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

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):  # Looping through every row
        symbol = columns[0][line]  # Setting symbol to the first column of the current row
        for column in columns:  # Loop through each column and check for the symbol
            symbol_to_check = column[line]  # The symbol to check is equal to column at the current row
            if symbol != symbol_to_check:  # If symbols aren't the same
                break  # Break out the loop, check the next line
        else:
            winnings += values[symbol] * bet  # If no break, user wins multiplier for the symbol times their bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines




def get_slot_machine_spin(rows, cols, symbols): #Passing 3 parameters to the function.
    # Populating the symbols to go into the slot machine
    all_symbols = []  # Define our list of symbols
    for symbol, symbol_count in symbols.items():  #.items gives key and value associated. symbol = key and symbol_count = item.
        for _ in range(symbol_count):  # Loop through the symbol count (value) e.g. 2 for A, 4 for B
            all_symbols.append(symbol)  # Add the item (key) to the list


    # Populating the slot machine itself
    columns = []  # Defining our columns list.
    for _ in range(cols):  # Generating a column for every column we have e.g. 3 times for 3 columns
        column = []  # Empty list where each our selected values will eventually be stored in each column.
        current_symbols = all_symbols[:]  # current_symbols are = to a copy of the all symbols list (2 A's, 4 B's, 6 C's, 8 D's.)
        for _ in range(rows):  # Loop through number of values we need to generate (rows on slot machine)
            value = random.choice(current_symbols)  # Select random value from the current_symbols list
            current_symbols.remove(value)  # Once selected, remove this value from the current_symbols list
            column.append(value)  # Add the value to the column list

        columns.append(column)  # Add the column to the columns list

    return columns
    # Columns are returned in the following format:
    # [A, B, B]
    # [B, D, D]
    # They currently look like rows, with each row being a specific column in the slot machine.


def print_slot_machine(columns):

    # Flipping the columns so they actually appear as rows:
    for row in range(len(columns[0])):  # For every row we have
        for i, column in enumerate(columns):  # Looping through all the items inside 'columns'. Enumerate gives index as well as the item.
            if i != len(columns) - 1:  # Checking this isn't the last value in the row
                print(column[row], end=" | ")  # Print the value at the first row of that column. End tells print statement what to end line with.
            else:
                print(column[row], end="")  # Print last value without the pipe

        print()  # Brings the row down to another line







def deposit():
    while True:  # Continue to loop until we break out of it
        amount = input("What would you like to deposit? $")  # Ask user how much they want to deposit
        if amount.isdigit():  # isdigit checks if amount entered is a whole number
            amount = int(amount)  # Convert amount to an integer
            if amount > 0:  # If this amount is greater than 0
                break  # Break out of the loop
            else:  # Otherwise
                print("Amount must be greater than 0.")  # Loop restarts with the following message
        else:  # If the input entered fails the isdigit check
            print("Please enter a number.")  # Loop restarts with the following message

    return amount  # Function returns the amount


def get_number_of_lines():
    while True:  # Continue to loop until we break out of it
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})")  # Ask user to enter number of lines between 1 and the max number defined at top of program.
        if lines.isdigit():  # isdigit checks if amount entered is a whole number
            lines = int(lines)  # Convert amount to an integer
            if 1 <= lines <= MAX_LINES:  # If this amount is <=1 and <= MAX_LINES global variable
                break  # Break out of the loop
            else:  # Otherwise
                print("Enter a valid number of lines")  # Loop restarts with the following message
        else:  # If the input entered fails the isdigit check
            print("Please enter a number.")  # Loop restarts with the following message

    return lines  # Function returns the amount


def get_bet():
    while True:  # Continue to loop until we break out of it
        amount = input("What would you like to bet on each line? $")  # Ask user how much they want to bet
        if amount.isdigit():  # isdigit checks if amount entered is a whole number
            amount = int(amount)  # Convert amount to an integer
            if MIN_BET <= amount <= MAX_BET:  # If this amount is between the min bet and max bet global variables
                break  # Break out of the loop
            else:  # Otherwise
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")  # Loop restarts with the following message
        else:  # If the input entered fails the isdigit check
            print("Please enter a number.")  # Loop restarts with the following message

    return amount  # Function returns the amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't not have enough to bet that amount. Current balance: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")



main()



# Need to finish; 32:07  
