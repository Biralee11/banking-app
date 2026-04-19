from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, email, phone_number, interest_rate, account_type):
        super().__init__(account_holder, account_number, balance, email, phone_number, account_type)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: £{self.balance}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nInterest Rate: {self.interest_rate * 100}%\nAccount Type: {self.account_type}"
    
    def to_dict(self):
        return {"account_holder": self.account_holder, "account_number": self.account_number, "balance": self.balance, "email": self.email, "phone_number": self.phone_number, "interest_rate": self.interest_rate, "account_type": self.account_type}
    
    def apply_interest(self):
        self.balance = self.balance + (self.balance * self.interest_rate)