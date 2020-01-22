list = []

for x in range(10):
    list.append(1 if x % 2 == 0 else 0)     # that s generator in the parentheses

print(list)

# ---------------------------

lst = [1 if x % 2 == 0 else 0 for x in range(10)]

print(lst)
