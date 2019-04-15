# < =  25 euro - 15 % Discount
# > 25 to =< 50 - 25 % Discount
# > 50 - 35 % Discount
# new list

chaos = ["new price:2", "old price:12", "new price:45", "old price:23", "old price:41", "new price:33"]


new = []
for i in chaos:
    i = i.split(":")
    new.append(i)
print(new)

for row in new:
    row[1] = int(row[1])
    if 'old price' in row:
        if row[1] <= 25:
            row[1] = row[1]*0.85
        elif 25 <= row[1] <= 50:
            row[1] = row[1]*0.75
        elif row[1] > 50:
            row[1] = row[1]*0.65
print(new)

all_prices = []
for item in new:
    all_prices.append(item[1])
print(all_prices)
print(sum(all_prices))
