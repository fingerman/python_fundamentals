class Gladiator:
    def __init__(self, name, technique, skill):
        self.name = name
        self.technique = technique
        self.skill = int(skill)

    def __hash__(self):
        return self.name.__hash__

    def __eq__(self, other):
        return self.name == other.name


line = input()
gladiators_list = []


while line != "Ave Cesar":




    line = input()
