import pytest
from src.CheckPassword import CheckPassword


@pytest.fixture
def password():
    return CheckPassword("assword")

@pytest.fixture
def password_factory():
    def _make(password_value):
        return CheckPassword(password_value)
    return _make