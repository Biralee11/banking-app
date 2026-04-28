import pytest
from unittest.mock import MagicMock
from savings_account import SavingsAccount
from current_account import CurrentAccount
from strategies import SimpleInterestStrategy, CompoundInterestStrategy


@pytest.fixture
def savings_account():
    return SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, SimpleInterestStrategy())
@pytest.fixture
def current_account():
    return CurrentAccount("James Carlwell", "57995436", 1200, "jamesCark@yahoo.co.uk", "07898762365", 500)
@pytest.fixture
def savings_dict_account():
    return {"account_holder": "Kcee Michael", "account_number": "30443685", "balance": 1200.0, "email": "kcee.michael@gmail.com", "phone_number": "07345789092", "interest_rate": 0.05, "interest_strategy": "SimpleInterestStrategy", "account_type": "savings"}
@pytest.fixture
def current_dict_account():
    return {"account_holder": "James Carlwell", "account_number": "57995436", "balance": 1200.0, "email": "jamesCark@yahoo.co.uk", "phone_number": "07898762365", "overdraft_limit": 500.0, "account_type": "current"}


def test_deposit(savings_account):
    savings_account.deposit(500)
    assert savings_account.balance == 1700

def test_deposit_invalid(savings_account):
    savings_account.deposit(0)
    assert savings_account.balance == 1200
    savings_account.deposit(-100)
    assert savings_account.balance == 1200

def test_withdraw(savings_account):
    savings_account.withdraw(200)
    assert savings_account.balance == 1000

def test_withdraw_insufficient_funds(savings_account):
    savings_account.withdraw(1500)
    assert savings_account.balance == 1200

def test_transfer():
    sender = MagicMock()
    receiver = MagicMock()
    
    sender.withdraw.return_value = True
    withdraw_result = sender.withdraw(500)
    
    if withdraw_result == True:
        receiver.deposit.return_value = True
        receiver.deposit(500)
    
    sender.withdraw.assert_called_with(500)
    receiver.deposit.assert_called_with(500)

def test_savings_apply_interest(savings_account):
    savings_account.apply_interest()
    assert savings_account.balance == 1260

def test_current_overdraft(current_account):
    current_account.withdraw(1400)
    assert current_account.balance == -200

def test_current_overdraft_exceeded(current_account):
    current_account.withdraw(1800)
    assert current_account.balance == 1200

def test_to_dict_savings(savings_account):
    account_dict = savings_account.to_dict()
    assert account_dict == {"account_holder": "Kcee Michael", "account_number": "30443685", "balance": 1200.0, "email": "kcee.michael@gmail.com", "phone_number": "07345789092", "interest_rate": 0.05, "interest_strategy": "SimpleInterestStrategy", "account_type": "savings"}

def test_to_dict_current(current_account):
    account_dict = current_account.to_dict()
    assert account_dict == {"account_holder": "James Carlwell", "account_number": "57995436", "balance": 1200.0, "email": "jamesCark@yahoo.co.uk", "phone_number": "07898762365", "overdraft_limit": 500.0, "account_type": "current"}

def test_from_dict_savings(savings_dict_account):
    account_object = SavingsAccount.from_dict(savings_dict_account)
    assert account_object == SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, SimpleInterestStrategy())

def test_from_dict_current(current_dict_account):
    account_object = CurrentAccount.from_dict(current_dict_account)
    assert account_object == CurrentAccount("James Carlwell", "57995436", 1200, "jamesCark@yahoo.co.uk", "07898762365", 500)