class User:
    age = 0  # ustaliliśmy podstawowy wiek

    def print_age(self, message):
        print(message, 'wiek', self.age, self.name)

    def another_method(self):
        pass


user1 = User()
user2 = User()

user1.name = 'Arek'
user1.age = 24
user1.print_age('dodatkowy teskt')

user2.name = 'Mirek'
user2.age = 28
user2.print_age('dodatkowy teskt inny')

userList = [User(), User()]

userList[0].age = 20
userList[1].age = 30

userList[0].name = 'Franiu'
userList[1].name = 'Wiolka'

userList[0].print_age('')


class User:
    age = 0
    max = 40

    def message(self, message):
        print(message, self.name, 'wiek:', self.age, 'waga:', self.weight)


user1 = User()

user1.name = 'Arek'
user1.weight = 80
user1.age = 20
user1.message('wiadomosc')


userList = [User(), User(), User()]

userList[0].name = 'Jarek'
userList[0].weight = '40 kg'
userList[0].age = 16

userList[1].name = 'Maciek'
userList[1].weight = '80 kg'
userList[1].age = 21

userList[2].name = 'Dawid'
userList[2].weight = '100 kg'
userList[2].age = 31

userList[0].message('Prezentacja:')
userList[1].message('Prezentacja:')
userList[2].message('Prezentacja')
