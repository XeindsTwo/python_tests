import pytest

"""
Тесты на метод validatePassword:
1) Проверяет работу на длину строку
2) Проверяется наличие заглавных букв
3) Проверяется наличие цифр
"""
def test_password_short_password(password_factory):
    user = password_factory("abc1")

    with pytest.raises(ValueError) as exc_info:
        user.validatePassword()

    assert str(exc_info.value) == "Длина строки меньше 8 символов"


def test_password_with_alpha(password_factory):
    user = password_factory("fgdodfgkdfgodfg")

    with pytest.raises(ValueError) as exc_info:
        user.validatePassword()

    assert str(exc_info.value) == "В пароле не имеется заглавных букв"


def test_password_with_digit(password_factory):
    user = password_factory("Fggfdgfgdfg")

    with pytest.raises(ValueError) as exc_info:
        user.validatePassword()

    assert str(exc_info.value) == "В пароле не имеется цифр"


"""
Тесты на метод is_common_password 
(проверят, является ли простой пароль слишком простым):
1) На простой пароль должен возвращать True
2) На обычный пароль должен возвращать False
"""


def test_password_is_common_password_simple(password_factory):
    user = password_factory("qwErty")

    with pytest.raises(ValueError) as exc_info:
        user.is_common_password()

    assert str(exc_info.value) == "Слишком простой пароль"


def test_password_is_common_password_ordinary(password_factory):
    user = password_factory("Fdokdfg954")
    result = user.is_common_password()
    assert result is False
