def adder(*args, **kwargs):
    result = 0
    for num in args:
        result += num
    for item in kwargs.values():
        result += item
    return result
