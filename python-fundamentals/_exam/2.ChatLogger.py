inventory = []
line = input()

while line != "end":
    tokens = line.split(' ')
    command = tokens[0]
    message = tokens[1]
    if len(tokens) > 2:
        message2 = tokens[2]
    else:
        pass

    if len(tokens) > 3:
        message_add1 = tokens[2]
        message_add2 = tokens[3]
    else:
        pass

    if command == "Chat":
        inventory.append(message)

    if command == "Delete":
        if message in inventory:
            inventory.remove(message)

    if command == "Edit":
        if message in inventory:
            message_index = inventory.index(message)
            inventory[message_index] = message2
        else:
            pass

    if command == "Spam":
        for i in tokens[1:]:
            inventory.append(i)

    if command == "Pin":
        if message in inventory:
            inventory.remove(message)
            inventory.append(message)

    line = input()


for i in inventory:
    print(i)



'''
Chat John
Spam Let's go to the zoo
Edit zoo cinema
Chat tonight
Pin John
end



'''
