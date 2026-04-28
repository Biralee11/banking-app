# Banking CLI App

A command-line banking application built in Python, demonstrating advanced backend engineering concepts including OOP, design patterns, concurrency, and testing.

## Overview

This project started as a beginner Python CLI app and has been progressively refactored through intermediate and advanced levels. It serves as a portfolio project showcasing real-world Python backend skills.

## Features

- Create savings and current accounts with validation
- Deposit, withdraw, and transfer funds
- Apply interest using pluggable strategies (Simple or Compound)
- Automatic email and SMS notifications on transactions
- Persistent storage via JSON
- Full test suite with pytest

## Advanced Concepts Demonstrated

- **Metaclass** — `AccountMeta` enforces required class attributes across all account types
- **Descriptors** — `BalanceDescriptor` and `CurrentAccountBalanceDescriptor` control balance access and validation
- **Decorator Factory** — `@log_transaction` accepts a log level argument for configurable transaction logging
- **Observer Pattern** — notifications fire automatically on deposits and withdrawals
- **Strategy Pattern** — interest calculation is swappable per account without modifying core logic
- **Mixin** — `LogMixin` adds reusable logging behaviour across all account classes
- **Asyncio** — demonstrated in `async_demo.py` for simulating concurrent transaction processing
- **Type Hints** — applied throughout the codebase
- **Abstract Base Class** — `BankAccount` cannot be instantiated directly, enforces interface on child classes

## Project Structure

```
banking_app/
    bank_account.py         # Abstract base class, metaclass, decorator factory
    savings_account.py      # SavingsAccount with strategy-based interest
    current_account.py      # CurrentAccount with overdraft support
    bank_transaction.py     # Context manager for transfers
    descriptors.py          # BalanceDescriptor and CurrentAccountBalanceDescriptor
    mixins.py               # LogMixin
    notifications.py        # EmailNotification and SMSNotification
    strategies.py           # SimpleInterestStrategy and CompoundInterestStrategy
    async_demo.py           # Asyncio transaction simulation
    main.py                 # CLI entry point
    test_banking_app_pytest.py  # Pytest test suite with fixtures and mocking
    requirements.txt
```

## Technologies

- Python 3.14
- pytest
- unittest.mock
- asyncio
- JSON for persistence

## Installation

1. Clone the repository:
```
git clone https://github.com/Biralee11/banking-app.git
cd banking-app
```

2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Running the App

```
python main.py
```

## Running the Tests

```
pytest test_banking_app_pytest.py
```

## Running the Async Demo

```
python async_demo.py
```
