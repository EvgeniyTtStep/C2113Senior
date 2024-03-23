class Example:
    num = 10
    _num = 11
    __num = 12

    def __init__(self):
        self.text = "Num"
        self._text = "_Num"
        self.__text = "__Num"

    def info(self):
        print(self.text, self.num)
        print(self._text, self._num)
        print(self.__text, self.__num)


class Next(Example):
    def next_info(self):
        print(self.text, self.num)
        print(self._text, self._num)
        print(self.__text, self.__num)


print("Example")
example = Example()
example.info()

print("Next")
next = Next()
next.next_info()
