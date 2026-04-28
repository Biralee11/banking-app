from abc import ABCMeta, abstractmethod
from typing import Optional
from descriptors import BalanceDescriptor
from mixins import LogMixin


def log_transaction(log_level):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{log_level} - Transaction Started - {func.__name__}")
            result = func(*args, **kwargs)
            if result == True:
                print(f"{log_level} - Transaction Complete - {func.__name__}")
            else:
                print(f"{log_level} -Transaction Failed - {func.__name__}")    
            return result
        return wrapper
    return my_decorator

class AccountMeta(ABCMeta):
    def __new__(cls, name, bases, dct):
        if bases == () and "currency" not in dct:
            raise AttributeError('missing attribute "currency"')      
        return super().__new__(cls, name, bases, dct)

class BankAccount(LogMixin, metaclass=AccountMeta):
    currency = "GBP"
    balance = BalanceDescriptor()
    def __init__(self, account_holder, account_number, balance, email, phone_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self._balance = balance
        self.email = email
        self.phone_number = phone_number
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
    
    @log_transaction("INFO")
    def deposit(self, amount: float) -> Optional[bool]:
        if amount <= 0:
            print("deposit amount must be greater than zero.")
            return False
        else:
            self.balance = self.balance + amount
            print("Deposit successful!")
            self.notify_observers(f"Deposit of £{amount} made, balance is now £{self.balance}")
            return True
    
    @log_transaction("WARNING")
    def withdraw(self, amount: float) -> Optional[bool]:
        if amount > self.balance:
            print(f"Insufficient funds. Current balance is £{self.balance}.")
            return False
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False
        else:
            self.balance = self.balance - amount
            print("Withdraw Successful!")
            self.notify_observers(f"Withdrawal of £{amount} made, balance is now £{self.balance}")
            return True