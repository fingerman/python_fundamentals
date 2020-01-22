class User:
    def __init__(self, name, age):
        self.name = name #public attribute
        self.__age = age #private attribute

    def __privMethod(self): #private method
        print("I am a private Method!")

    def pubMethod(self): #public method
        print("I am a public Method!")

user1=User("max", 30)

print(user1._User__age)
user1._User__privMethod()
user1.pubMethod()
