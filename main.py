from savings_account import SavingsAccount
from current_account import CurrentAccount
from bank_transaction import BankTransaction
from random import randint
import json
import re

def fetch_accounts(accounts):
    for account in accounts:
        yield account

def display_menu():
    print("==== Banking App ====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View Account")
    print("6. View All Accounts")
    print("7. Update Account Details")
    print("8. Apply Interest")
    print("9. Save to File")
    print("10. Close Account")
    print("11. Exit")
    print("=====================")

def create_account(accounts):
    print("Type 'exit' at any time to cancel.")
    while True:
        user_input = input("Enter Account Type (Savings/Current): ")
        if user_input.lower() == "exit":
            return
        account_type = user_input
        if account_type.lower() == "savings" or account_type.lower() == "current":
            break
        else:
            print("Invalid account type. Please enter Savings or Current enter exit to go back.")

    while True:
        user_input = input("Enter Name: ")
        if user_input.lower() == "exit":
                return
        elif re.search(r"^[a-zA-Z]+( [a-zA-Z]+)+$", user_input):
            account_holder = user_input
            break
        else:
            print("Invalid Name, please enter a valid name or enter exit to go back")

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
            print("Invalid input, please enter a number or or enter exit to go back.")
    
    while True:
        user_input = input("Enter Email: ")
        if user_input.lower() == "exit":
                return
        elif re.search(r"^[\w.]+@\w+(\.\w+)+$", user_input):
            email = user_input
            break
        else:
            print("Invalid email, please enter a valid email or enter exit to go back")

    while True:
        user_input = input("Enter Phone Number: ")
        if user_input.lower() == "exit":
                return
        elif re.search(r"^07\d{9}$", user_input):
            phone_number = user_input
            break
        else:
            print("Invalid Phone Number, please enter a valid phone number or enter exit to go back")

    if account_type.lower() == "savings":
        while True:
            user_input = input("Enter Interest Rate: ")
            if user_input.lower() == "exit":
                return
            try:
                interest_rate = float(user_input)
                if interest_rate < 0:
                    print("Interest Rate must be greater than zero\nenter a number greater than zero or enter exit to go back.")
                    continue
                break
            except ValueError:
                print("Invalid input, please enter a number or enter exit to go back.")
        account_number = str(randint(0, 99999999)).zfill(8)
        account = SavingsAccount(account_holder, account_number, opening_balance, email, phone_number, interest_rate, account_type)

    elif account_type.lower() == "current":
        while True:
            user_input = input("Enter Overdraft Limit: ")
            if user_input.lower() == "exit":
                return
            try:
                overdraft_limit = float(user_input)
                if overdraft_limit < 0:
                    print("Overdraft Limit must be greater than zero\nenter a number greater than zero or enter exit to go back.")
                    continue
                break
            except ValueError:
                print("Invalid input, please enter a number or enter exit to go back.")
        account_number = str(randint(0, 99999999)).zfill(8)
        account = CurrentAccount(account_holder, account_number, opening_balance, email, phone_number, overdraft_limit, account_type)

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
        if account.account_number == account_number:
            account_found = True
            while True:
                user_input = input("Enter Deposit: ")
                if user_input.lower() == "exit":
                    return
                else:
                    try:
                        deposit_amount = float(user_input)
                        result= account.deposit(deposit_amount)
                        if result:
                            return True
                    except ValueError:
                        print("Invalid input, please enter a number or enter exit to go back.")
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
        if account.account_number == account_number:
            account_found = True
            while True:
                user_input = input("Enter Withdraw Amount: ")
                if user_input.lower() == "exit":
                    return
                try:
                    withdraw_amount = float(user_input)
                    result = account.withdraw(withdraw_amount)
                    if result:
                        return True
                except ValueError:
                    print("Invalid input, please enter a number or enter exit to go back.")
                    continue
    if not account_found:
        print("Account not found")

def transfer(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number Of Sender: ")
    if user_input.lower() == "exit":
            return
    sender_account_number = user_input
    user_input = input("Enter Account Number of Receiver: ")
    if user_input.lower() == "exit":
            return
    receiver_account_number = user_input
    sender_account_found = False
    receiver_account_found = False
    for account in accounts:    
        if account.account_number == sender_account_number:
            sender_account_found = True
            sender_account = account
        elif account.account_number == receiver_account_number:
            receiver_account_found = True
            receiver_account = account
    if sender_account_found == True and receiver_account_found == True:   
        while True:
            user_input = input("Enter amount to transfer: ")
            if user_input.lower() == "exit":
                return
            try:
                transfer_amount = float(user_input)
                with BankTransaction(sender_account, "transfer") as transaction:
                    withdraw_result = sender_account.withdraw(transfer_amount)
                    if withdraw_result:
                        deposit_result = receiver_account.deposit(transfer_amount)
                        if deposit_result:
                            print("Transfer Complete!")
                            return True
            except ValueError:
                print("Invalid input, please enter a number or enter exit to go back.")
                continue
    if not sender_account_found:
        print("Sender account not found")
    elif not receiver_account_found:
        print("Receiver not found")
  
def view_account(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number: ")
    if user_input.lower() == "exit":
            return
    account_number = user_input
    account_found = False
    for account in accounts:
        if account.account_number == account_number:
            account_found = True
            print("=====================")
            print(account)
            print("=====================")
            break
    if not account_found:
        print("Account not found")

def view_all_accounts(accounts):
    if not accounts:
        print("No accounts found")
    else:
        gen_accounts = fetch_accounts(accounts)
        for account in gen_accounts:
            print("=====================")
            print(account)
            print("=====================")

def update_account_details(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number: ")
    if user_input.lower() == "exit":
            return
    account_number = user_input
    account_found = False
    for account in accounts:
        if account.account_number == account_number:
            account_found = True
            name_update = False
            email_update = False
            phone_number_update = False
            while True:
                print("1.Update Name")
                print("2.Update Email")
                print("3.Update Phone Number")
                user_input = input("Enter option: ")
                if user_input == "1":
                    user_input = input("Enter Name: ")
                    if re.search(r"^[a-zA-Z]+( [a-zA-Z]+)+$", user_input):
                        account_holder = user_input
                        account.account_holder = account_holder
                        name_update = True
                        continue
                    else:
                        print("Invalid Name")
                        name_update = False
                        continue

                elif user_input == "2":
                    user_input = input("Enter email: ")
                    if re.search(r"^[\w.]+@\w+(\.\w+)+$", user_input):
                        email = user_input
                        account.email = email
                        email_update = True
                        continue
                    else:
                        print("Invalid email")
                        email_update = False
                        continue

                elif user_input == "3":
                    user_input = input("Enter Phone Number: ")
                    if re.search(r"^07\d{9}$", user_input):
                        phone_number = user_input
                        account.phone_number = phone_number
                        phone_number_update = True
                        continue
                    else:
                        print("Invalid Phone Number")
                        phone_number_update = False
                        continue

                elif user_input.lower() == "exit" and (name_update == True or email_update == True or phone_number_update == True):
                    return True
                elif user_input.lower() == "exit":
                    return

                else:
                    print("Invalid Choice, enter a number between 1-3 or enter exit to go back")
                    continue

    if not account_found:
        print("Account not found")

def apply_interest(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number: ")
    if user_input.lower() == "exit":
            return
    account_number = user_input
    account_found = False
    for account in accounts:
        if account.account_number == account_number:
            account_found = True
            if account.account_type.lower() == "savings":
                result = account.apply_interest()
                if result:
                    print("Interest applied successfully")
                    return True
            else:
                print("Interest does not apply to current account")
    if not account_found:
        print("Account not found")

def save_to_file(accounts):
        with open("accounts.json", "w") as file:
            accounts_dicts = [account.to_dict() for account in accounts]
            json.dump(accounts_dicts, file)
        print("Accounts saved successfully!")

def close_account(accounts):
    print("Type 'exit' at any time to cancel.")
    user_input = input("Enter Account Number: ")
    if user_input.lower() == "exit":
            return
    account_number = user_input
    account_found = False
    for account in accounts:
            if account.account_number == account_number:
                accounts.remove(account)
                print("Account closed successfully!")
                return True
            
    if not account_found:
        print("Account not found")
  
def load_from_file():
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
            accounts_to_object = list()
            for account in accounts:
                account_holder = account["account_holder"]
                account_number = account["account_number"]
                balance = account["balance"]
                email = account["email"]
                phone_number = account["phone_number"]
                account_type = account["account_type"] 
                if account_type.lower() ==  "savings":
                    interest_rate = account["interest_rate"]
                    accounts_to_object.append(SavingsAccount(account_holder, account_number, balance, email, phone_number, interest_rate, account_type))
                elif account_type.lower() ==  "current":
                    overdraft_limit = account["overdraft_limit"]
                    accounts_to_object.append(CurrentAccount(account_holder, account_number, balance, email, phone_number, overdraft_limit, account_type))
            return accounts_to_object
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
            result = transfer(accounts)
            if result:
                unsaved_changes = True
        elif choice == "5":
            view_account(accounts)
        elif choice == "6":
            view_all_accounts(accounts)
        elif choice == "7":
            result = update_account_details(accounts)
            if result:
                unsaved_changes = True
        elif choice == "8":
            result = apply_interest(accounts)
            if result:
                unsaved_changes = True
        elif choice == "9":
            save_to_file(accounts)
        elif choice == "10":
            result = close_account(accounts)
            if result:
                unsaved_changes = True
        elif choice == "11":
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
            print("Invalid choice, please enter either number between 1-11")

if __name__ == "__main__":
    main()