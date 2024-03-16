class Student:
    count = 0

    def __init__(self, name, age, phone, height=155):
        self.name = name
        self.age = age
        self.phone = phone
        self.height = height
        Student.count += 1  # count належить до класу а не до об'єкту

    def student_info(self):
        print("name = ", self.name)
        print("age = ", self.age)
        print("height = ", self.height)
        print("count = ", self.count, "\n")


# створення об'єкту first_student
first_student = Student(name="Bob", age=11, phone=123, height=150)
first_student.student_info()
# print("name = ", first_student.name)
# print("age = ", first_student.age)
# print("height = ", first_student.height)
# print("count = ", first_student.count)

# створення об'єкту second_student
second_student = Student("Max", 12, 456, 160)
second_student.student_info()
# print("name = ", second_student.name)
# print("age = ", second_student.age)
# print("height = ", second_student.height)
# print("count = ", second_student.count)

third_student = Student("Vito", 13, 789)
third_student.student_info()
# print("name = ", third_student.name)
# print("age = ", third_student.age)
# print("height = ", third_student.height)
# print("count = ", third_student.count)
