import pytest
from src.BankAccount import BankAccount

@pytest.fixture
def account():
    return BankAccount("Иван", balance=1000)