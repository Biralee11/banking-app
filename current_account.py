from bank_account import BankAccount, log_transaction
from descriptors import CurrentAccountBalanceDescriptor

class CurrentAccount(BankAccount):
    account_type = "current"
    balance = CurrentAccountBalanceDescriptor()
    def __init__(self, account_holder, account_number, balance, email, phone_number, overdraft_limit):
        super().__init__(account_holder, account_number, balance, email, phone_number)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: £{self.balance}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nOverdraft Limit: {self.overdraft_limit}\nAccount Type: {self.account_type}"

    def to_dict(self):
        return {"account_holder": self.account_holder, "account_number": self.account_number, "balance": self.balance, "email": self.email, "phone_number": self.phone_number, "overdraft_limit": self.overdraft_limit, "account_type": self.account_type}
    
    @classmethod
    def from_dict(cls, dict_account):
        account_holder = dict_account["account_holder"]
        account_number = dict_account["account_number"]
        balance = dict_account["balance"]
        email = dict_account["email"]
        phone_number = dict_account["phone_number"]
        overdraft_limit = dict_account["overdraft_limit"]
        return cls(account_holder, account_number, balance, email, phone_number, overdraft_limit)
    
    @log_transaction("WARNING")
    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            print(f"Insufficient funds. Current balance is £{self.balance}.")
            return False
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero")
            return False
        else:
            self.balance = self.balance -  amount
            print("Withdrawal Successful!")
            self.notify_observers(f"Withdrawal of £{amount} made, balance is now £{self.balance}")
            return True