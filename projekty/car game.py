from pyexpat import model
from turtle import speed
from random import randint


class Car:
    def __init__(self, mark, model, color, age, maxSpeed) -> None:
        self.mark = mark
        self.model = model
        self.color = color
        self.age = age
        self.maxSpeed = maxSpeed
        self.speed = 0

    def speed_draw(self):
        self.speed = randint(0, self.maxSpeed)
        return self.speed


car1 = Car('Ford', 'Mustang', 'White', 2011, 200)
car2 = Car('Chevrolet', 'Camaro', 'Black', 2013, 250)

if car1.speed_draw() > car2.speed_draw():
    print(car1.model, 'win this race')
else:
    print(car2.model, 'win this race')
