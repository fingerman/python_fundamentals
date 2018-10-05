
animal = input()

switcher = {
    "dog": "mammal",
    "crocodile": "reptile",
    "tortoise": "reptile",
    "snake": "reptile",
}

print(switcher.get(animal, "unknown"))



