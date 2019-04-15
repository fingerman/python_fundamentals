chaos = ["new price:2", "old price:12", "new price:45", "old price:23", "new price:41", "old price:33"]
new = []
for i in chaos:
    i = int(i.split(":")[1])
    print(i)
    new.append(i)
print(new)