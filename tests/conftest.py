import pytest
from src.BankAccount import BankAccount

@pytest.fixture(scope="module")
def account():
    acc = BankAccount("Иван", balance=1000)
    print(f"\nСоздан объект, id={id(acc)}")
    return acc