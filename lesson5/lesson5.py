class Animal:
    age = 5


class Cat(Animal):
    height = 20


class Dog(Animal):
    height = 40
    age = 10


class ChiHuaHua(Dog):
    weight = 100
    height = 0.5
    def __init__(self):
        print("ChiHuaHua")
        print(self.age)
        print(self.height)
        print(self.weight)


cat = Cat()
dog = Dog()

print("Cat")
print(cat.height)
print(cat.age)

print("Dog")
print(dog.height)
print(dog.age)
