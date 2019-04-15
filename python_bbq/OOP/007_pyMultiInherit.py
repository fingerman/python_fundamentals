#Python Multiple Inheritance
#One class extending more than one class is called multiple inheritance
#in multi-level inheritance the superclass may also inherit another super class
#definition of the class starts here


class Person:
    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    # defining class methods
    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    # end of class definition


# defining another class
class Student:
    def __init__(self, studentId):
        self.studentId = studentId

    def get_id(self):
        return self.studentId


class Resident(Person, Student): # extends both Person and Student class
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)


# Create an object of the subclass
resident1 = Resident('John', 30, '102')
resident1.show_name() # Methode der Klasse Person
print(resident1.get_id()) # Methode der Klasse Student
