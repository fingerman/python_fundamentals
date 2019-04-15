#Type of methods in Python
#Static methods

#Class methods
#A class method is the one which can be called only with the instance of an Object.
#These methods usually define the behavior of an object and
#modify the object’s properties or instance variables.
#There are two ways to create class methods in Python:

#Using classmethod(function)
#Using @classmethod annotation
#Using classmethod() look non-Pythonic and hence, in newer Python versions,
#we can use the @classmethod annotation decorator for making class methods.
#Providing Boilerplate

class DateTime(object):

    def __init__(self, day=10, month=10, year=2000):
        self.day = day
        self.month = month
        self.year = year

#Including class methods
#Now, we will enhance the boilerplate code in the last section and include
#a class method in it which can receive a date as a String and return a real
#Date instance. Let’s look at a code snippet:


@classmethod
def from_string(cls, string_date):
    day, month, year = map(int, string_date.split('-'))
    myDate = cls(day, month, year)
    return myDate
#Notice that this method will act as a constructor for this class as well due
#to the reason that this method takes in class as its reference.
#Also, it actually constructs the class instance from a String.
#Let’s look at a code snippet on how this constructor can be put to use:
dateObj = DateTime.from_string('20-05-1994')

#How does it differ from static method?
#Static methods are the one which belongs to a class
#rather than a particular instance of that class

@staticmethod
def is_valid_date(date_as_string):
    day, month, year = map(int, date_as_string.split('-'))
    return day <= 31 and month <= 12 and year <= 3999
#This can be put to use like:
is_valid_date = Date.is_date_valid('20-05-1994')
#Here, we don’t do anything with any instance of the class and just check
#if something is appropriate to be converted to the instance of that class.
#Our complete class code looks like:

class DateTime(object):

    def __init__(self, day=10, month=10, year=2000):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, string_date):
        day, month, year = map(int, string_date.split('-'))
        myDate = cls(day, month, year)
        return myDate

    @staticmethod
    def is_valid_date(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

dateObj = DateTime.from_string('20-05-1994')
is_valid_date = DateTime.is_valid_date('20-05-1994')
print(is_valid_date)

# output: True
#The @classmethod annotation decorator is used to create factory methods as
#they can take any input and provide a class object based on the parameters
#and processing. Using this decorator, it is possible to create as many
#constructors for a class which behaves as factory constructors.
