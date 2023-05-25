class User:
    def __init__(self, name, age, schoolClass,) -> None:
        self.name = name
        self.age = age
        self.schoolClass = schoolClass

    def __str__(self):
        return self.name + ", age: " + str(self.age) + ", class: " + str(self.schoolClass)


class Students:
    def __init__(self) -> None:
        Mark = User('Mark', 10, 4)
        Jacob = User('Jacob', 12, 6)
        Joe = User('Joe', 14, 8)


print(Students)
