
people = {1 : {'name': 'John', 'age': 27, 'sex': 'Male'},
          2 : {'name': 'Marie', 'age': 27, 'sex': 'Female'}}

print(people.items())

for k, v in people.items():
    print(v.keys())



print("-----------------")
print(people[1]['name'])

# update dict values
people[1].update(name='Pencho')
print(people[1]['name'])

# compare nested dictionary values
print(people[1]['age'] == people[2]['age'])
print(people[1]['age'] < 25)

print("\nadd entry to nested dictionary")
people[1].update({"height": 186})
print(people.items())

d = {325:1, 321:0, 322:3}
smallest = min(d.items(), key=lambda x: x[0])
print(smallest)