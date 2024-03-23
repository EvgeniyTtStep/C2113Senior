class Car:
    def __init__(self):
        print("Car", end=" ")

    def about(self):
        print("I am parent class Car")


class Nissan(Car):
    def __init__(self):  # alt + enter
        super().__init__()
        print("nissan")
        super().about()


nissan = Nissan()
