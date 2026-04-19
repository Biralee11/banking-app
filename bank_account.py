from abc import ABC, abstractmethod

def log_transaction(func):
    def wrapper(*args, **kwargs):
        print(f"Transaction Started - {func.__name__}")
        result = func(*args, **kwargs)
        if result == True:
            print(f"Transaction Complete - {func.__name__}")
        else:
            print(f"Transaction Failed - {func.__name__}")    
        return result
    return wrapper

class BankAccount(ABC):
    def __init__(self, account_holder, account_number, balance, email, phone_number, account_type):
        self.account_holder = account_holder
        self.account_number = account_number
        self._balance = balance
        self.email = email
        self.phone_number = phone_number
        self.account_type = account_type

    @abstractmethod
    def __str__(self):
        pass

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            print("Balance must be a number.")
            return
        if value >= 0:
            self._balance = value
        else:
            print("Balance cannot be less than zero.")

    @abstractmethod
    def to_dict(self):
        pass
    
    @log_transaction
    def deposit(self, amount):
        if amount <= 0:
            print("deposit amount must be greater than zero.")
            return False
        else:
            self.balance = self.balance + amount
            print("Deposit successful!")
            return True
    
    @log_transaction
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance is £{self.balance}.")
            return False
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False
        else:
            self.balance = self.balance - amount
            print("Withdraw Successful!")
            return True