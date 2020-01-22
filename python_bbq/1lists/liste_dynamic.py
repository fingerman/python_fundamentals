# lst = [i for i in range(1, 10)]
# print(lst)

lst1 = [[j for j in range(0, 3)] for i in range(1, 10)]
print(lst1)

lst_out= []
lst_in = []

for i in range(1, 10):
    lst_out.append(lst_in)
for j in range(0, 3):
    lst_in.append(j)
print(lst_out)



print("----------")
lst2 = [j for j in range(0, 3) for i in range(1, 10)]
print(lst2)

lst_2 = []
for j in range(0, 3):
    for i in range(1, 10):
        lst_2.append(j)
print(lst_2)
