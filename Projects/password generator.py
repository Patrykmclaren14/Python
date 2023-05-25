import random


def password_generator(letters, numerals, characters):
    x = 0
    howManyCharacters = int(
        input('Enter how many characters will be in password:'))
    bag = letters + numerals + characters
    password = []
    while x < howManyCharacters:
        x += 1
        password.append(bag[random.randint(0, len(bag)-1)])
    connectPassword = "".join(password)
    return connectPassword


letters = []
numerals = []
characters = []
for letter in range(97, 123):
    letters.append(chr(letter))

for number in range(0, 10):
    numerals.append(str(number))

for code in range(33, 48):
    characters.append(chr(code))

print(password_generator(letters, numerals, characters))
