from CheckPassword import CheckPassword

user = CheckPassword("Ffgdfgd2fg")

user.validatePassword()
print(user.password_strength())
print(user.is_common_password())