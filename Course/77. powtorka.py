from random import randint


class Rocket:
    def __init__(self) -> None:  # podpisanie zmiennych do inita
        self.altitude = 0
        self.speed = 0

    def speedUp(self, worth):
        self.speed = worth ** 2

    def moveUp(self):  # dwie funkcje ktore sie wykonuja
        self.altitude += 1

    def __str__(self):
        return 'Rakieta jest na wysokości: ' + str(self.altitude) + ' i osiąga szybkość: ' + str(self.speed)

    def get_distance(self, rocket):
        return rocket.altitude - rocket.altitude


# wytworzenie rakiet jako obiekt
# print(rockets)


class RocketBoard:
    def __init__(self) -> None:
        self.rockets = [Rocket() for _ in range(5)]
        for _ in range(30):
            x = randint(0, 4)
            self.rockets[x].moveUp()

        for x in range(0, 4):
            self.rockets[x].speedUp(self.rockets[x].altitude)

    def __getitem__(self, key):
        return self.rockets[key]


board = RocketBoard()

print(board[0].altitude - board[1].altitude)
