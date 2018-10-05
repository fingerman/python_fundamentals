inventory = [int(item) for item in input().split(' ')]
line = input()

while line != "Mort":
    tokens = line.split(' ')
    command = tokens[0]
    num1 = int(tokens[1])
    if len(tokens) > 2:
        num2 = int(tokens[2])
    else:
        pass

    if command == "Add":
        inventory.append(num1)

    if command == "Remove":
        if num1 in inventory:
            inventory.remove(num1)
        elif num1 not in inventory:
            if num1 <= len(inventory):
                inventory.pop(num1)
    if command == "Replace":
        if len(tokens) > 2:
            if num1 in inventory:
                num1_index = inventory.index(num1)
                inventory[num1_index] = num2
            else:
                pass
        else:
            pass
    if command == "Increase":
        value = 0
        if num1 not in inventory:
            value = inventory[-1]
            inventory = [x+value for x in inventory]
        else:
            value = num1
            for i in inventory:
                if value > i:
                    i = value
                    inventory = [x+value for x in inventory]

    if command == "Collapse":
        if num1 in inventory:
            val_remove = num1
            for i in inventory:
                if val_remove < i:
                    i = val_remove
                    inventory = [i for i in inventory if i >= val_remove]

    line = input()


print(" ".join(map(str, inventory)))



