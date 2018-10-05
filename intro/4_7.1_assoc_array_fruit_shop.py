fruit = input()
day = input().lower()
amount = float(input())
workdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
if day == 'saturday' or day == 'sunday':
    fruit_cost = {'banana': 2.7, 'apple': 1.25, 'orange': 0.9,
                  'grapefruit': 1.6, 'kiwi': 3, 'pineapple': 5.6, 'grapes': 4.2}
else:
    fruit_cost = {'banana': 2.5, 'apple': 1.2, 'orange': 0.85, 'grapefruit': 1.45,
                  'kiwi': 2.7, 'pineapple': 5.5, 'grapes': 3.85}
for f, c in fruit_cost.items():
    if f == fruit and day in workdays:
        print(round(amount * c, 2))
        break
if fruit not in fruit_cost.keys() or day not in workdays:
    print('error')