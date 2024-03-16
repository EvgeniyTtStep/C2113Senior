class Student:
    def __init__(self, name, age, phone, height):
        self.name = name
        self.age = age
        self.phone = phone
        self.height = height


first_student = Student(name="Bob", age=11, phone=123, height=150)

print("name = ", first_student.name)
print("age = ", first_student.age)
print("height = ", first_student.height)

second_student = Student("Max", 12, 456, 160)

print("name = ", second_student.name)
print("age = ", second_student.age)
print("height = ", second_student.height)
