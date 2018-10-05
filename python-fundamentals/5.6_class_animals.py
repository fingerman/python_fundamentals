class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs
        self.sound = "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
        self.info = f"Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}"

    def produce_sound(self):
        return self.sound




class Cat:
    def __init__(self, name, age, intelligence_quotent):
        self.name = name
        self.age = age
        self.intelligence_quotent = intelligence_quotent
        self.sound = 'I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.'
        self.info = f'Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotent}'

    def produce_sound(self):
        return self.sound


class Snake:
    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cruelty_coefficient = cruelty_coefficient
        self.sound = 'I\'m a Sophistisnake, and I will now produce a sophisticated sound! Honey, I\'m home.'
        self.info = f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}'

    def produce_sound(self):
        return self.sound


line = input()
animals_list = []
sounds_list = []

while line != "I'm your Huckleberry":
    line_list = line.split(' ')
    if len(line_list) > 2:
        class_name, name, age, parameter = line.split(' ')
        if class_name == "Dog":
            animals_list.append(Dog(name, age, parameter))
        if class_name == "Cat":
            animals_list.append(Cat(name, age, parameter))
        if class_name == "Snake":
            animals_list.append(Snake(name, age, parameter))

    if len(line_list) == 2:
        command, pet_name = line.split(' ')
        sounds_list.append(pet_name)
    line = input()


for sounds in sounds_list:
    for animal in animals_list:
        if sounds == animal.name:
            print(animal.produce_sound())


for animal in animals_list:
    if animal.__class__.__name__ == "Dog":
        print(animal.info)
for animal in animals_list:
    if animal.__class__.__name__ == "Cat":
        print(animal.info)
for animal in animals_list:
    if animal.__class__.__name__ == "Snake":
        print(animal.info)

'''
6.	Animals *---------------------------------
You have been given the task to create classes for several sophisticated animals.
Create a class Dog which has a name (string), age (int) and number_of_legs (int).
Create a class Cat which has a name (string), age (int) and intelligence_quotient (int).
Create a class Snake which has a name (string), age(int) and cruelty_coefficient (int).
Create a method in each class which is called produce_sound(). The method should print on the console a string depending on the class:
•	If it’s a Dog, you should print “I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.”
•	It it’s a Cat, you should print “I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.”
•	If it’s a Snake, you should print “I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.”
Now for the real deal. You will receive several input commands, which will register animals or make them produce sounds, until you receive the command “I’m your Huckleberry”.
The commands will be in the following format:
{class} {name} {age} {parameter}
The class will be either “Dog”, “Cat” or “Snake”. The name will be a simple string, which can contain any ASCII character BUT space. The age will be an integer. The parameter, will be an integer. Depending on the class it would either be number of legs, IQ, or cruelty coefficient.
Register each animal, and keep them in collections, by your choice, so that you can ACCESS THEM BY NAME. You will most likely need 3 collections, to store the different animals inside them.
Between the register commands you might receive a command in the following format:
talk {name}
You must then make the animal with the given name, produce a sound.

When you receive the ending command, you should print every animal in the following format:
•	If it’s a Dog, you should print “Dog: {name}, Age: {age}, Number Of Legs: {numberOfLegs}”
•	It it’s a Cat, you should print “Cat: {name}, Age: {age}, IQ: {intelligenceQuotient}”
•	If it’s a Snake, you should print “Snake: {name}, Age: {age}, Cruelty: {crueltyCoefficient}”
Print first the Dogs, then the Cats, and lastly – The Snakes.
Constraints
•	You can assume that there will be no duplicate names (even in different animals).
•	All input data will be valid. There will be no invalid input lines.
•	The name in the talk command, will always be existent.
-----------------------------------------------------------------
Examples
Input
	
Dog Sharo 3 4
Cat Garfield 5 200
Snake Alex 25 1000
talk Sharo
talk Garfield
talk Alex
I'm your Huckleberry	

Output:
I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.
I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.
I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.
Dog: Sharo, Age: 3, Number Of Legs: 4
Cat: Garfield, Age: 5, IQ: 200
Snake: Alex, Age: 25, Cruelty: 1000


Dog Bau 5 10
Cat Myau 5 100
Dog Georgi 20 1000
Cat Bojo 4 20
talk Bojo
I'm your Huckleberry	

Output:
I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.
Dog: Bau, Age: 5, Number Of Legs: 10
Dog: Georgi, Age: 20, Number Of Legs: 1000
Cat: Myau, Age: 5, IQ: 100
Cat: Bojo, Age: 4, IQ: 20

'''
