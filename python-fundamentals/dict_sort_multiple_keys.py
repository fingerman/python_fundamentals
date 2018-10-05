class person:
    def __init__(self, name):
        self.name = name


d_multiple = {person("Pierre"): 42,
              person("Anne"): 33,
              person('Mandrigon'): 24,
              person('Samuel'): 27,
              person('Wolfgang'): 29,
              person('Riko'): 41,
              person('Riko'): 42,
              person('Riko'): 43}



# sort by value in descending order
sorted_dict = dict(sorted(
    d_multiple.items(), key=lambda x: -x[1]))

#print(d_multiple.values())

print(sorted_dict)

