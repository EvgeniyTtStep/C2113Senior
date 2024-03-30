class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"Your work = {self.work}. \nOur work = {work}."


helper = Helper("homework")
print(helper("classwork"))
