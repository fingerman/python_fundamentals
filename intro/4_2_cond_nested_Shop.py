''' input:
coffee
Varna
2
output:
0.9
'''




''' input:
12
f
output:
Miss
'''

product = input()
city = input()
n = float(input())
price = 0
if product == "coffee":
    if city == "Sofia":
        price = 0.50
    if city == "Plovdiv":
        price = 0.40
    if city == "Varna":
        price = 0.45
if product == "water":
    if city == "Sofia":
        price = 0.80
    if city == "Plovdiv":
        price = 0.70
    if city == "Varna":
        price = 0.70
if product == "beer":
    if city == "Sofia":
        price = 1.20
    if city == "Plovdiv":
        price = 1.15
    if city == "Varna":
        price = 1.10
if product == "sweets":
    if city == "Sofia":
        price = 1.45
    if city == "Plovdiv":
        price = 1.30
    if city == "Varna":
        price = 1.35
if product == "peanuts":
    if city == "Sofia":
        price = 1.60
    if city == "Plovdiv":
        price = 1.50
    if city == "Varna":
        price = 1.55
print(n * price)
