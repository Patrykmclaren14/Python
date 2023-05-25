from unicodedata import name


class Bank:
    def __init__(self) -> None:
        self.money = 0

    def deposit(self, amount):
        self.money += amount

    def try_withdraw(self, amount):
        self.money -= amount

    def __str__(self) -> str:
        return 'You have ' + str(self.money) + ' on the bank account'


user = Bank()
user.deposit(500)
user.deposit(5000)
print(user)
