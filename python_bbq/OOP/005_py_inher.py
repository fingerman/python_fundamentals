#Python Inheritance
#Python Inheritance Terminologies
#Superclass: The class from which attributes and methods will be inherited.
#Subclass: The class which inherits the members from superclass.
#Method Overriding: Redefining the definitions of methods in subclass
#which was already defined in superclass.


#Line:1, definition of the superclass starts here
class Person:
    #initializing the variables
    name = ""
    age = 0

    #defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    #defining class methods
    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    #Line: 25, end of superclass definition

#definition of subclass starts here
class Student(Person):
    studentId = ""

    def __init__(self, studentName, studentAge, studentId):
        Person.__init__(self, studentName, studentAge)  # Calling the superclass constructor and sending values of attributes.
        self.studentId = studentId

    def get_id(self):
        return self.studentId  #returns the value of student id
#end of subclass definition


# Create an object of the superclass
#person1 = Person("Richard", 23)
#call member methods of the objects
#person1.show_age()
# Create an object of the subclass
student1 = Student("Max", 22, "102")
print(student1.get_id())
student1.show_name() # Methode aus Superklasse
