try:
    cars = ["Car1", "Car2"]
    print(10 / 5)
    print("End")
    print(cars[2])
except ZeroDivisionError as error:
    print("ZeroDivision ERRRRRORORROROR", error)
except NameError as error:
    print("Name ERRRRRORORROROR", error)
except IndexError as error:
    print("Index ERRRRRORORROROR", error)

print("End program")

try:
    cars = ["Car1", "Car2"]
    print(10 / 0)
    print("End")
    print(cars[2])
except (ZeroDivisionError, NameError, IndexError) as error:
    print("ERRRRRORORROROR", error)

print("End program")
