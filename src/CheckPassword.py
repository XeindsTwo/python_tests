class CheckPassword:
    common_passwords = {
        "123456",
        "12345678",
        "123456789",
        "password",
        "qwerty",
        "111111",
        "123123",
        "abc123",
        "admin",
        "letmein",
        "welcome",
        "iloveyou",
        "000000",
        "passw0rd",
        "qwerty123"
    }

    def __init__(self, password_user: str):
        self.password_user = password_user

    def validatePassword(self):
        password = self.password_user

        if password is None:
            raise ValueError("Пароль не может быть пустым")

        if len(password) < 8:
            raise ValueError("Длина строки меньше 8 символов")

        hasUpper = False
        hasDigit = False

        for char in password:
            if char.isupper():
                hasUpper = True
            elif char.isdigit():
                hasDigit = True

        if not hasUpper:
            raise ValueError("В пароле не имеется заглавных букв")

        if not hasDigit:
            raise ValueError("В пароле не имеется цифр")

        return True

    def is_common_password(self):
        if self.password_user.lower() in self.common_passwords:
            raise ValueError("Слишком простой пароль")
        return False

    def password_strength(self):
        password = self.password_user

        length = len(password)
        has_digit = any(c.isdigit() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_special = any(not c.isalnum() for c in password)

        if length >= 12 and has_digit and has_upper and has_special:
            return "strong"
        elif length >= 10 and has_digit and has_upper:
            return "medium"
        else:
            return "weak"