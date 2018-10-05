''' input:
12
f
output:
Miss
'''

age = float(input())
sex = input()
'''if sex == "m" and age >= 16:
    print("Mr.")
if sex == "m" and age < 16:
    print("Master")

if sex == "f" and age >= 16:
    print("Ms.")
if sex == "f" and age < 16:
    print("Miss")
'''
if sex == "m":
    if age >= 16:
        print("Mr.")
    if age < 16:
        print("Master")
if sex == "f":
    if age >= 16:
        print("Ms.")
    if age < 16:
        print("Miss")

