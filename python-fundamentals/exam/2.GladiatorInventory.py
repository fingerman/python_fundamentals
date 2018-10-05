inventory = [str(item) for item in input().split(' ')]
line = input()

while line != "Fight!":
    tokens = line.split(' ')
    command = tokens[0]
    weapon = tokens[1]

    if command == "Upgrade":
        tokensUpgrade = weapon.split('-')
        weaponUpgrade = tokensUpgrade[0]
        if len(tokensUpgrade) > 1:
            weaponFeature = tokensUpgrade[1]

            if weaponUpgrade in inventory:
                weaponIndex = inventory.index(weaponUpgrade)
                weaponIndexInsert = weaponIndex + 1
                inventory.insert(weaponIndexInsert, weaponUpgrade + ":" + weaponFeature)
        else:
            pass
    if command == "Buy":
        if weapon not in inventory:
            inventory.append(weapon)
        else:
            pass
    if command == "Trash":
        if weapon in inventory:
            inventory.remove(weapon)
        else:
            pass
    if command == "Repair":
        if weapon in inventory:
            inventory.remove(weapon)
            inventory.append(weapon)
        else:
            pass

    line = input()

print(" ".join(inventory))



'''
Problem 2 – Gladiator Inventory
As a gladiator, Pesho has cool Inventory. He loves to buy new equipment. You are given Pesho`s inventory with all of his equipment -> strings, separated by whitespace. Until you receive "Fight!" you will be receiving commands which Pesho does with his inventory.
You may receive the following commands:
•	Buy {equipment}
•	Trash {equipment}
•	Repair {equipment}
•	Upgrade {equipment}-{upgrade}
If you receive Buy command, you should add the equipment at last position in the inventory, but only if it isn`t bought already.
If you receive Trash command, delete the equipment if it exists.
If you receive Repair command, you should Repair the equipment if it exists and place it on last position.
If you receive Upgrade command, you should check if the equipment exists and insert after it the upgrade in the following format: "{equipment}:{upgrade}";
Input / Consrtaints
You will receive input in several lines. Each line is a command:
•	One the first line, you will receive Pesho`s inventory – sequence of equipment names, separated by space.
•	Each following line, until you receive "Fight!" will be a command. 
Output
•	As output you must print Pesho`s inventory. 
Constraints
•	The command will always be valid.
•	The equipment and Upgrade will be strings and will contain any character, except '-'.
•	Allowed working time / memory: 100ms / 16MB.

Scroll down to see examples.
 
Examples
Input	

SWORD Shield Spear
Buy Bag
Trash Shield
Repair Spear
Upgrade SWORD-Steel
Fight!

Output
SWORD SWORD:Steel Bag Spear	
-----------------------------

Input

SWORD Shield Spear
Trash Bow
Repair Shield
Upgrade Helmet-V
Fight!	

Output
SWORD Spear Shield	



'''