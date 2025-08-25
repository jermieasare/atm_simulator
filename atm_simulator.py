import datetime

user_pin = 3333
current_balance= 30000.0
transaction_history = [ ]


print("WELCOME TO MEST ATM")
print("Please insert your ATM card ")
# Ask user to insert the card
user_card_name= input("Please enter your name>> ")
user_card_number = int(input("Enter your serial number>> "))


# pin authentication (create function to use while and if loops)
def pin_authentication():
    attempts = 0
    while attempts <3:

        pin = int(input("Enter your pin>> "))
        try:
            if pin == user_pin:
                print("Login Successful")
                break
            else:
                print("Authentication Failed")
        except ValueError:
            print("Invalid pin - Try again")
    return pin
pin_authentication()

def withdrawal():
    global current_balance
    withdrawal_amount= float(input("Enter the amount you want to withdraw>> "))
    if withdrawal_amount  <= 0:
        print("Invalid input")
        return
    if withdrawal_amount <= current_balance:
        current_balance -= withdrawal_amount
        print("Withdrawal successful, please take your cash")
        print_receipt("Withdrawal", withdrawal_amount)
        add_to_history("Withdrawal", withdrawal_amount, current_balance)
    else:
        print("Insufficient balance")

def deposit():
    global current_balance
    deposit_amount= float(input("Enter the amount you want to deposit>> "))
    if deposit_amount >= 0:
        current_balance += deposit_amount
        print("Deposit successful")
        print_receipt("Deposit", deposit_amount)
        add_to_history("Deposit", deposit_amount, current_balance)
        return
    else:
        print("Invalid input")

def add_to_history(type, amount, balance):
    transaction = {
        "type": type,
        "amount": amount,
        "balance": balance,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    transaction_history.append(transaction)

def show_history():
    print("--------------------------")
    print("    TRANSACTION HISTORY")
    print("--------------------------")
    if not transaction_history:
        print("No transactions yet")
    else:
        for transaction in transaction_history:
            print(
                f"Date: {transaction['date']}\n"
                f"Transaction: {transaction['type']}\n"
                f"Amount: GHS{transaction['amount']}\n"
                f"Balance: GHS {transaction['balance']}\n"
                f"--------------------------"
                )

def print_receipt(transaction_type, amount):
    print("\n--------------------------")
    print("       ATM RECEIPT")
    print("--------------------------")
    print(f"Transaction: {transaction_type}")
    print(f"Amount: GHS {amount:,.2f}")
    print(f"Balance: GHS {current_balance:,.2f}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("--------------------------\n")

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")

    options = input("Choose an option>> ")
    if options == "1":
        print(f"Balance is GHS {current_balance}")
    elif options == "2":
        deposit()
    elif options == "3":
        withdrawal()
    elif options == "4":
        show_history()
    elif options == "5":
        print("Thank You for using MEST ATM. Goodbye👋")
        break        
    else:
        print("Choose from options 1-5")