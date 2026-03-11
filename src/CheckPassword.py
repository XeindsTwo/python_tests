class CheckPassword:
    def __init__(self, password_user: str):
        self.password_user = password_user

    def validatePassword(self):
        hasUpper = False
        hasDigit = False

        for char in self.password_user:
            if len(self.password_user) < 8:
                raise ValueError("Длина строки меньше 8 символов")
            elif char.isalpha() and char.isupper():
                hasUpper = True
            elif char.isdigit():
                hasDigit = True

        if not hasUpper:
            raise ValueError("В пароле не имеется заглавных букв")
        elif not hasDigit:
            raise ValueError("В пароле не имеется цифр")

        return True
