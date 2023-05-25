class User:
    def __init__(self, age, name) -> None:
        print(
            "Jestem inicjalizatorem, ktory wywoluje sie zawsze podczas konstrukcji obiektu")
        self.age = age
        self.name = name
        self.ageInFuture = age + 1

    def print_age(self, message):
        print(message, 'wiek', self.age, self.name)


user1 = User(30, 'Arek')
user2 = User(24, 'Mirek')


user1.print_age('dodatkowy teskt')


user2.print_age('dodatkowy teskt inny')

print(user1.ageInFuture)


class User:
    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name
        self.ageInFuture = age + 10

    def print_all(self, message):
        print(message, 'wiek:', self.age, 'imie:', self.name,
              'wiek w przyszlosci:', self.ageInFuture)


user1 = User(20, 'Wojtek')

user1.print_all('Prezentacja >>>')
