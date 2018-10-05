# Multiple identical keys in a Python dict

# If you have a list, you can only have one element at each number -
# there's just a single positon [0], a single [1] and so on.
# That's clear, and natural to understand. With a dict in Python
# (like a hash in Perl or an associative array in PHP), it's peceived wisdom
# that you can only have one element with a paricular name.

# Let's see an example - setting up a dict:
control = {"Andrew" : "Cambridge", "Barabara" : "Bloomsbury", "Andrew": "Corsica"}
print(control)


# it replaces the original Andrew element with a new element of the same name. 
# So that although we've added three elements,

# if I use mutable objects as my keys, then I can create multiple identical objects


class person(object):
    def __init__(self, name):
        self.name = name


# I can then set up my dict as follows:

alternate = {person("Andrew") : "Cambridge", person("Barabara") : "Bloomsbury", person("Andrew"): "Corsica"}
print(alternate.items())

#  loop through all the keys via the keys method:
for staff in alternate.keys():
    print(staff.name, "lives in", alternate[staff])

#  add yet another "Andrew" to our dict.
alternate[person("Andrew")] = "Tignabruiach"

#  change keys

for staff in alternate.keys():
    staff.name = 0
    print(staff.name)







