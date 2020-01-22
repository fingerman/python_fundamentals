T = [[3 - i for i in range(3)] for j in range(3)]
print(T)

Outside = []
Inside = []

for j in range(3):
    Outside.append(Inside)
for i in range(3):
    i = 3-i
    Inside.append(i)
print(Outside)

## -----------------------------------

T1 = [3 - i for i in range(3) for j in range(3)]
print(T1)

T2 = []
for i in range(3):
    i = 3 - i
    for j in range(3):
        T2.append(i)
print(T2)