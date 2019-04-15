list_str = ['berLin', 'HamBurg', 'PytHoN iSt coOl', 'Katze iSt Kein hunD']

wordsA = [[i] for i in list_str]
print(wordsA)

wordsB = [i.split(' ') for i in list_str]
print(wordsB)


wordsC = [i.capitalize() for i in list_str]
print(wordsC)

