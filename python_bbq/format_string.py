# string formating - 4 methods

name = "Axel"
age = 30
print(name + " is " + str(age) + " years old.")
print("%s is %s years old." %(name, age)) # 1) old style
print("{} is {} years old.".format(name, age))# 2) new style
print(f"{name} is {age} years old.") # 3) string interpolation - python 3.6 or later

# which formating method to use?
# python 3.6 or newer & no user supplied information : string interpolation
# python older than 3.6 & no user supplied information : new style

