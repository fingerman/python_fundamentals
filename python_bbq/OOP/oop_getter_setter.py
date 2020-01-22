class Member:
    def __init__(self, age = 0):
        self._age = age
# getter method
    def get_age (self):
        return self._age
# setter method
    def set_age (self, x):
        self._age = x

Uwe = Member()
# setting the age using setter
Uwe.set_age(21)
# retrieving age using getter
print(Uwe.get_age ())
print(Uwe._age )