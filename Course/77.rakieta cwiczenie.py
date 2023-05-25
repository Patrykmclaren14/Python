import random


class Rocket:
    def __init__(self) -> None:
        self.altitude = 0
        self.speed = 0

    def moveUp(self):
        self.altitude += 1

    def speedUp(self, worth):
        self.speed += worth ** 2

    def __str__(self):
        x = 0
        x += 1
        # wazne zagadnienie kiedy odwolujemy sie do klasy
        return 'Rakieta jest na wysokosci: ' + str(self.altitude)


rockets = [Rocket() for _ in range(5)]


for _ in range(0, 10):
    x = random.randint(0, 4)
    rockets[x].moveUp()

for x in range(0, 5):
    rockets[x].speedUp(rockets[x].altitude)

for rocket in rockets:
    print(rocket)
