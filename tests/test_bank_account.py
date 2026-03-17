import pytest

from tests.conftest import account


@pytest.mark.parametrize("amount, expected_balance", [
    (100, 1100),
    (500, 1500),
    (1000, 2000),
    (5000, 6000)
])
def test_deposit_increases_balance(account, amount, expected_balance):
    account.deposit(amount)
    assert account.balance == expected_balance


@pytest.mark.parametrize("bad_amount", [0, -50, -200])
def test_deposit_invalid_amount_raises_value_error(account, bad_amount):
    with pytest.raises(ValueError):
        account.deposit(bad_amount)


def test_deposit_adds_transaction(account):
    account.deposit(500)
    assert account.get_transaction_count() == 1


def test_deposit_withdraw_transaction(account):
    account.withdraw(200)
    assert account.get_transaction_count() == 2