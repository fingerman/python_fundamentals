# < =  25 euro - 15 % Discount
# > 25 to =< 50 - 25 % Discount
# > 50 - 35 % Discount
# new list

# ls = [x if (condition) else None for x in ls]
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