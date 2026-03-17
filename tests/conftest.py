import pytest
from src.BankAccount import BankAccount

@pytest.fixture(scope="module")
def account():
    account = BankAccount("Амирус", balance=1000)
    print(f"\nСоздан объект, id={id(account)}")
    return account

@pytest.fixture(scope="module")
def account_readonly():
    account = BankAccount("Амирус", balance=1000)
    print(f"\nСоздан один объект на все тесты")
    return account