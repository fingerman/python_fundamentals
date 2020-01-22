class TelBuch():

    def __init__(self):
        self.__eintraege = {}

    def add(self, name, rufnummer):
        self.__eintraege[name] = rufnummer

    def get(self, name):
        if name in self.__eintraege:
            return self.__eintraege[name]
        else:
            return None

    # gibt die Objektinstanz zurück:
    def __str__(self):
        return str(self.__eintraege)

    # 2. Variante:
    def __repr__(self):
        return self.__str__()

buch = TelBuch()
buch.add("David", 1234565)
buch.add("Philipp", 451245)
#print(buch)
print(buch.get("David"))
