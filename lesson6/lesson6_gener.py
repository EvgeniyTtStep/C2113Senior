def foo(num):
    if type(num) != int:
        raise TypeError("You mast enter int value")
    else:
        return num * 2


# обробити виклик функції через try except у випадку error
try:
    res = foo("hello")
    print(res)
except TypeError as error:
    print("TypeError", error)
