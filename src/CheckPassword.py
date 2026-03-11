class CheckPassword:
    def __init__(self, password_user: str):
        self.password_user = password_user

    @staticmethod
    def validatePassword(password: str):
        hasUpper = False
        hasDigit = False

        if len(password) < 8:
            raise ValueError("Длина строки меньше 8 символов")

        for char in password:
            if char.isalpha() and char.isupper():
                hasUpper = True
            elif char.isdigit():
                hasDigit = True

        if not hasUpper:
            raise ValueError("В пароле не имеется заглавных букв")
        elif not hasDigit:
            raise ValueError("В пароле не имеется цифр")

        return True
