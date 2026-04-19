from bank_account import BankAccount, log_transaction

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, email, phone_number, overdraft_limit, account_type):
        super().__init__(account_holder, account_number, balance, email, phone_number, account_type)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: £{self.balance}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nOverdraft Limit: {self.overdraft_limit}\nAccount Type: {self.account_type}"
    
    @BankAccount.balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            print("Balance must be a number.")
            return
        if value >= (-self.overdraft_limit):
            self._balance = value
        else:
            print("Balance cannot be less than overdraft limit.")

    def to_dict(self):
        return {"account_holder": self.account_holder, "account_number": self.account_number, "balance": self.balance, "email": self.email, "phone_number": self.phone_number, "overdraft_limit": self.overdraft_limit, "account_type": self.account_type}
    
    @log_transaction
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
            return True