mixed = ["hola", "bola", "chola", 8, 6, (4, 5), "dsa", "Afrika", "Asien"]
continents = ["Afrika", "Antarktis", "Asien", "Europa"]


# common elements from both lists
for element in mixed:
    if element in continents:
        print(element)

num = 0
for element in mixed:
    if element in continents:
        num += 1
print(num)