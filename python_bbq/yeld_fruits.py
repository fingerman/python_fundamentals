def fruits():
    yield "Mango"
    yield "Orange"
    yield "Apple"
    yield "Strawberry"

allf = fruits()

for i in allf:
    print(i)

def foo():
    for i in range(0, 10):
        yield i
print(foo())
for i in foo():
    print(i)
print(foo())