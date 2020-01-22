continents = ["Afrika", "Antarktis", "Asien", "Europa"]

print('1 -----------------')
for i in continents:      # do not print anything
    if i == "Afrika":
        break
    print(i)

print('2 -----------------')

for i in continents:    # print "Afrika"
    print(i)
    if i == "Afrika":
        break

print('3 -----------------')

for i in continents:      # print without "Afrika"
    if i == "Afrika":
        continue
    print(i)




