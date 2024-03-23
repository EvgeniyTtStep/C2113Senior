class Comp:
    def calc(self):
        print("Calculating...")


class Display():
    def display(self):
        print("Display image to screen...")


class Phone(Comp, Display):
    pass


android = Phone()
android.calc()
android.display()
