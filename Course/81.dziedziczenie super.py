from multiprocessing import resource_tracker


class Bank:
    def __init__(self, balance) -> None:
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def try_withdraw(self, amount):
        self.balance -= amount

    def __str__(self) -> str:
        return 'You have ' + str(self.balance) + ' on the bank account'


class MinimumAccountBalance(Bank):
    def __init__(self, balance=0, minimumBalance=1000) -> None:
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def try_withdraw(self, amount):
        if self.balance - amount > self.minimumBalance:
            if self.balance > amount:
                self.balance -= amount
                return 'Udało się'
        else:
            return 'Nie udało się wypłacić z konta'


result = Bank(100)
result.deposit(5000)

print(result)

result2 = MinimumAccountBalance(1500, 1000)
result2.deposit(5000)
result2.try_withdraw(5499)

print(result2)
