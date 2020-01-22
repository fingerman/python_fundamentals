# Ask user for attributes values
class User:

    def __init__(self, name="", age=0):
        self.name = input(" Enter name: ")
        self.__age = input(" Enter age: ")

    def showName(self):
        print(" Name: ", self.name)

    def getAge(self):
        print(" Age: ", self.__age)

user1 = User()
print() # blanko
user1.showName()
user1.getAge()
print(user1._User__age) # user1.__age --> user1_User__age
