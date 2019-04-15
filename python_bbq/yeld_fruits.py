def fruits():
    yield "Mango"
    yield "Orange"
    yield "Apple"
    yield "Strawberry"

allf = fruits()

for i in allf:
    print(i)