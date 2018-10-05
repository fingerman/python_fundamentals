lostFights = int(input())
helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

helmetBreaks = lostFights // 2
swordBreaks = lostFights // 3
shieldBreaks = helmetBreaks // swordBreaks
shieldBreaks1 = lostFights // (shieldBreaks*6)

armorBreaks = shieldBreaks1 // 2


helmetTotalPrice = helmetBreaks * helmetPrice
swordTotalPrice = swordBreaks * swordPrice
shieldTotalPrice = shieldBreaks1 * shieldPrice
armorTotalPrice = armorBreaks * armorPrice

gladiatorExpenses = helmetTotalPrice + swordTotalPrice + shieldTotalPrice + armorTotalPrice


print("Gladiator expenses: {0:0.2f}".format(gladiatorExpenses) + " aureus")

'''
Problem 1 – Gladiator Expenses

As a gladiator, Pesho has to repair his broken equipment when he loses a fight. His equipment consists of 
helmet, sword, shield and armor. You will receive the Pesho`s lost fights count. 
Every second lost game, his helmet is broken.
Every third lost game, his sword is broken.
When both his sword and helmet are broken in the same lost fight, his shield also brakes.
Every second time, when his shield brakes, his armor also needs to be repaired. 
You will receive the price of each item in his equipment. Calculate his expenses for the year for
renewing his equipment. 
Input / Constraints
You will receive 5 lines:
•	First parameter – lost fights count – integer in the range [0, 1000].
•	Second parameter – helmet price - floating point number in range [0, 1000]. 
•	Third parameter – sword price - floating point number in range [0, 1000]. 
•	Fourth parameter – shield price - floating point number in range [0, 1000]. 
•	Fifth parameter – armor price - floating point number in range [0, 1000]. 
Output
•	As output you must print Pesho`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
•	Allowed working time / memory: 100ms / 16MB.
Input	
7
2
3
4
5	
Output: Gladiator expenses: 16.00 aureus
Input	
23
12.50
21.50
40
200	
Output: Gladiator expenses: 608.00 aureus

Comment
Trashed helmet -> 3 times
Trashed sword -> 2 times
Trashed shield -> 1 time
Total: 6 + 6 + 4 = 16.00 aureus;



'''



