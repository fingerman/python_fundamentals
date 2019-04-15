class Person:

    first_name = "FirstName"
    second_name = "SecondName"
    age = 1

    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def show_age(self):
        print(self.age)


class Student(Person):

    student_id = ""

    def __init__(self, f_name, sec_name, student_age, student_id):  # those arguments are just placce keepers
        Person.__init__(self, f_name, sec_name, student_age)
        self.student_id = student_id

    def get_name(self):
        return self.first_name

    def get_id(self):
        return self.student_id


student1 = Student("Max", "Beemer", 22, "102")
print(student1.__dict__)
student1.show_age()
person1 = Person("Hanna", "Arendt", 33)
print(person1.get_name)


