import pytest
from unittest.mock import MagicMock
from savings_account import SavingsAccount
from current_account import CurrentAccount
from strategies import SimpleInterestStrategy, CompoundInterestStrategy


@pytest.fixture
def savings_account():
    return SavingsAccount("Kcee Michael", "30443685", 1200, "kcee.michael@gmail.com", "07345789092", 0.05, SimpleInterestStrategy)

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