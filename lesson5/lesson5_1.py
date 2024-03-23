class App:
    def foo1(self):
        print("Foo1")

    def _foo2(self):
        print("Foo2")

    def __foo3(self):  # private
        print("Foo3")


class App1(App):
    def __init__(self):
        self.foo1()


app = App()
app.foo1()
app._foo2()
