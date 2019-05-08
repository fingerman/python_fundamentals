list_str = ['berLin', 'HamBurg', 'PytHoN iSt coOl', 'Katze iSt Kein hunD']

wordsA = [[i] for i in list_str]
print(wordsA)

wordsB = [i.split(' ') for i in list_str]
print(wordsB)

wordsC = [i.capitalize() for i in list_str]
print(wordsC)

print("#-----------------------------------")

l = [j for i in range(2, 8) for j in range(i*2, 50, i)]
print(l)

l1 = []
for i in range(2, 8):
    for j in range(i * 2, 50, i):
        l1.append(j)
print(l1)
