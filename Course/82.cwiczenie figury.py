class Rectangle:
    def __init__(self):
        self.solution = 0

    def calculation(self, a, b):
        self.solution = a * b

    def message(self) -> str:
        return 'surface: ' + str(self.solution)


object = Rectangle()
object.calculation(5, 20)
print(object.message())


class Square(Rectangle):
    def __init__(self) -> None:
        super().__init__()

    def calculation(self, a):
        self.solution = a ** 2


object = Square()
object.calculation(5)
print(object.message())


class Cube(Rectangle):
    def __init__(self):
        super().__init__()
        self.size = 0

    def calculation(self, a):
        self.solution = 6 * a ** 2
        self.size = a ** 3

    def message(self) -> str:
        return 'surface: ' + str(self.solution) + ' size: ' + str(self.size)


object = Cube()
object.calculation(5)
print((object.message()))
