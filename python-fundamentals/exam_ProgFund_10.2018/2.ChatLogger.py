'''

Task 2 – Chat Logger
Your task is to implement chat logger which works with commands.
You may receive the following commands:
•	Chat {message} - add the message at last position in the chat
•	Delete {messageToDelete} - delete the message if it exists
•	Edit {messageToEdit} {editedVersion} - update the message with the edited version
•	Pin {message} - find the given message and move it to the last index
•	Spam {message1} {message2} {messageN} - add all messages at the end of the chat
•	end - stop receiving commands
After the stop command, you should print the chat history starting from the first message.
Input
•	Until you receive "end" you will be receiving commands.
Output
•	As output you must print the chat starting from the first message.
Constraints
•	The command will always be valid.
•	The messages will always be one word strings.
•	Allowed working time / memory: 100ms / 16MB.
Examples
Input
Chat Hello
Chat darling
Edit darling Darling
Spam how are you
Delete Darling
end

Output
Hello
how
are
you

'''

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


