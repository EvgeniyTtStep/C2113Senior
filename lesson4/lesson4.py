class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_pass(self, human):
        self.passengers.append(human)

    def pass_info(self):
        if self.passengers != []:
            print("Names of", self.brand, "passengers")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print("No passengers in", self.brand)


jack = Human("Jack")
max = Human("Max")

car = Auto("Audi")
car.add_pass(jack)
car.add_pass(max)
car.pass_info()
