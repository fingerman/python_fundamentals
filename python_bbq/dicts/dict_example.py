'''
myDict = { "key1":"BMW", "key2":2008, "key3":"x3", "farbe":"rot" }


# declare dictionary
myDict["farbe"] = "blau"
print(myDict)
myDict1 = dict(key1="BMW",  key2=2008,  key3="x3" )  # declare with constructor
print(myDict1)

'''
#############################################

my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd':4 }
for item in my_dict:
    print(item)

# get the first value

print(list(my_dict.values())[0])

print(my_dict.get('a'))