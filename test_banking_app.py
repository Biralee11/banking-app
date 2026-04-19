import unittest
from savings_account import SavingsAccount
from current_account import CurrentAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, "savings")
        account.deposit(500)
        self.assertEqual(account.balance, 1700)


    def test_deposit_invalid(self):
        account = SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, "savings")
        account.deposit(0)
        self.assertEqual(account.balance, 1200)
        account.deposit(-100)
        self.assertEqual(account.balance, 1200)

    def test_withdraw(self):
        account = SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, "savings")
        account.withdraw(200)
        self.assertEqual(account.balance, 1000)

    def test_withdraw_insufficient_funds(self):
        account = SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, "savings")
        account.withdraw(1500)
        self.assertEqual(account.balance, 1200)

    def test_savings_apply_interest(self):
        account = SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, "savings")
        account.apply_interest()
        self.assertEqual(account.balance, 1260)

    def test_current_overdraft(self):
        account = CurrentAccount("James Carlwell", "57995436", 1200, "jamesCark@yahoo.co.uk", "07898762365", 500, "current")
        account.withdraw(1400)
        self.assertEqual(account.balance, -200)

    def test_current_overdraft_exceeded(self):
        account = CurrentAccount("James Carlrwell", "57995436", 1200, "jamesCark@yahoo.co.uk", "07898762365", 500, "current")
        account.withdraw(1800)
        self.assertEqual(account.balance, 1200)

    def test_to_dict_savings(self):
        account = SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, "savings")
        account_dict = account.to_dict()
        self.assertEqual(account_dict, {"account_holder": "Kcee Michael", "account_number": "30443685", "balance": 1200.0, "email": "kcee.michael@gmail.com", "phone_number": "07345789092", "interest_rate": 0.05, "account_type": "savings"})

    def test_to_dict_current(self):
        account = CurrentAccount("James Carlwell", "57995436", 1200, "jamesCark@yahoo.co.uk", "07898762365", 500, "current")
        account_dict = account.to_dict()
        self.assertEqual(account_dict, {"account_holder": "James Carlwell", "account_number": "57995436", "balance": 1200.0, "email": "jamesCark@yahoo.co.uk", "phone_number": "07898762365", "overdraft_limit": 500.0, "account_type": "current"})