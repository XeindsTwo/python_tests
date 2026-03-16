class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        if not owner:
            raise ValueError("Имя владельца не может быть пустым")
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")
        self.balance += amount
        self.transactions.append(("deposit", amount))

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))

    def get_transaction_count(self):
        return len(self.transactions)