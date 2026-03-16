import pytest

# (100, 1100)  -> amount=100, expected_balance=1100
# (500, 1500)  -> amount=500, expected_balance=1500
# (1000, 2000) -> amount=1000, expected_balance=2000
@pytest.mark.parametrize("amount, expected_balance", [
    (100, 1100),
    (500, 1500),
    (1000, 2000)
])
def test_deposit_increase_balance(account, amount, expected_balance):
    account.deposit(amount)

    assert account.balance == expected_balance

@pytest.mark.parametrize("bad_amount", [0, -50, -100])
def test_negative_one(account, bad_amount):
    with pytest.raises(ValueError) as exc_info:
        account.deposit(bad_amount)

    assert str(exc_info.value) == "Сумма пополнения должна быть больше нуля"
