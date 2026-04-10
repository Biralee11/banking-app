from random import randint
import json

def display_menu():
    print("==== Banking App ====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Account")
    print("5. View All Accounts")
    print("6. Save to File")
    print("7. Close Account")
    print("8. Exit")
    print("=====================")

def create_account(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Name: ")
    if user_input.lower() == "exit":
            return
    account_holder = user_input

    while True:
        user_input = input("Enter Account Type (Savings/Current): ")
        if user_input.lower() == "exit":
            return
        account_type = user_input
        if account_type.lower() == "savings" or account_type.lower() == "current":
            break
        else:
            print("Invalid account type. Please enter Savings or Current.")

    while True:
        user_input = input("Enter Opening Balance: ")
        if user_input.lower() == "exit":
            return
        try:
            opening_balance = float(user_input)
            if opening_balance < 0:
                print("Balance must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a number.")

    account_number = str(randint(0, 99999999)).zfill(8)
    account = {"account_holder": account_holder, "account_type": account_type, "balance": opening_balance, "account_number": account_number}
    accounts.append(account)
    print("Account created successfully!")
    return True

def deposit(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number: ")
    if user_input.lower() == "exit":
            return
    account_number = user_input
    account_found = False
    for account in accounts:
        if account["account_number"] == account_number:
            while True:
                user_input = input("Enter Deposit: ")
                if user_input.lower() == "exit":
                    return
                try:
                    deposit_amount = float(user_input)
                    if deposit_amount <= 0:
                        print("Deposit amount must be greater than zero.")
                        continue
                    else:
                        account["balance"] = account["balance"] + deposit_amount
                        print("Deposit successful!")
                        return True
                except ValueError:
                    print("Invalid input, please enter a number.")
                    continue

    if not account_found:
            print("Account not found")

def withdraw(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number: ")
    if user_input.lower() == "exit":
            return
    account_number = user_input
    account_found = False
    for account in accounts:
        if account["account_number"] == account_number:
            while True:
                user_input = input("Enter Withdraw Amount: ")
                if user_input.lower() == "exit":
                    return
                try:
                    withdraw_amount = float(user_input)
                    if withdraw_amount > account["balance"]:
                        print(f"Insufficient funds. Current balance is £{account["balance"]}")
                        continue
                    elif withdraw_amount <= 0:
                        print("Withdrawal amount must be greater than zero.")
                        continue
                    else:
                        account["balance"] = account["balance"] - withdraw_amount
                        print("Withdraw successful!")
                        return True
                except ValueError:
                    print("Invalid input, please enter a number.")
        
    if not account_found:
        print("Account not found")

def view_account(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number: ")
    if user_input.lower() == "exit":
            return
    account_number = user_input
    account_found = False
    for account in accounts:
        if account["account_number"] == account_number:
            print("=====================")
            print(f"Account Holder: {account["account_holder"]}")
            print(f"Account Number: {account["account_number"]}")
            print(f"Balance: £{account["balance"]}")
            print(f"Account Type: {account["account_type"]}")
            print("=====================")
            account_found = True
            break
    if not account_found:
        print("Account not found")

def view_all_accounts(accounts):
    if not accounts:
        print("No accounts found")
    else:
        for account in accounts:
            print("=====================")
            print(f"Account Holder: {account["account_holder"]}")
            print(f"Account Number: {account["account_number"]}")
            print(f"Balance: £{account["balance"]}")
            print(f"Account Type: {account["account_type"]}")
            print("=====================")

def save_to_file(accounts):
        with open("accounts.json", "w") as file:
            json.dump(accounts, file)
        print("Accounts saved successfully!")

def close_account(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number: ")
    if user_input.lower() == "exit":
            return
    account_number = user_input
    account_found = False
    for account in accounts:
            if account["account_number"] == account_number:
                accounts.remove(account)
                print("Account closed successfully!")
                return True
            
    if not account_found:
        print("Account not found")
  
def load_from_file():
    try:
        with open("accounts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    accounts = load_from_file()
    unsaved_changes = False
    running = True
    while running:
        display_menu()
        choice = input("Enter a choice: ")
        if choice == "1":
            result = create_account(accounts)
            if result:
                unsaved_changes = True
        elif choice == "2":
            result = deposit(accounts)
            if result:
                unsaved_changes = True
        elif choice == "3":
            result = withdraw(accounts)
            if result:
                unsaved_changes = True
        elif choice == "4":
            view_account(accounts)
        elif choice == "5":
            view_all_accounts(accounts)
        elif choice == "6":
            save_to_file(accounts)
        elif choice == "7":
            result = close_account(accounts)
            if result:
                unsaved_changes = True
        elif choice == "8":
            if unsaved_changes:
                while True:
                    confirm = input("You have unsaved changes. Save before exiting? (yes/no): ")
                    if confirm.lower() == "yes":
                        save_to_file(accounts)
                        break
                    elif confirm.lower() == "no":
                        break
                    else:
                        print("Invalid account input. Please enter yes or no.")
            running = False
        else:
            print("Invalid choice, please enter either number between 1-8")

if __name__ == "__main__":
    main()