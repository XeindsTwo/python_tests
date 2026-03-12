import pytest
from src.CheckPassword import CheckPassword

def test_password_short_password(password_factory):
    user = password_factory("abc1")

    # Act - Проверяем что пробрасывается исключение
    with pytest.raises(ValueError) as exc_info:
        user.validatePassword()

    # Assert - Дополнительная проверка на текст ошибки
    assert str(exc_info.value) == "Длина строки меньше 8 символов"

def test_password_with_alpha(password_factory):
    user = password_factory("fgdodfgkdfgodfg")

    with pytest.raises(ValueError) as exc_info:
        user.validatePassword()

    assert str(exc_info.value) == "В пароле не имеется заглавных букв"