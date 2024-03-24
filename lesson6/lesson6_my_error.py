class MyError(BaseException):
    def __str__(self):
        return "Limit is exceeded error"


def check(num):
    if num > 100:
        raise MyError()
    else:
        return num * 10


res = check(5500)
print(res)
