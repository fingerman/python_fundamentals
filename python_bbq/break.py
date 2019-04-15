continents = ["Afrika", "Antarktis", "Asien", "Europa"]

for i in continents:      # print "Afrika"
    if i == "Afrika":
        break
    print(i)


for i in continents:    # do not print anything
    print(i)
    if i == "Afrika":
        break


for i in continents:      # print without "Afrika"
    if i == "Afrika":
        continue
    print(i)




