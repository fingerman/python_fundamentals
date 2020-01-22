# ls = [x if (condition) else None for x in ls]

# expression1 if condition else expression2

items = [2, 12, 45, 23, 41, 59, 52, 67, 90, 112, 33]

new_items = [x*0.85 if x < 25 else x for x in items]

print(new_items)

lst = []
for x in items:
    if x < 25:
        x *= 0.85
    else:
        x = x
    lst.append(x)
print(lst)