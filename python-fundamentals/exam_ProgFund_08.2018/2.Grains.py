
'''
Problem 2 – Grains of Sand
You have become an apprentice! Congratulations or maybe…… regrets. Since you are working for the almighty Anthropomorphic personification – Death he is known for his work of taking care for all the world’s sand watches, he seems to deal with this job pretty well, but you as a programmer want to help him, and make his job easier.
You are given all the grains of each sand watch in a sequence on a single line, separated by spaces. After that, you will receive commands that modify the grains in a different way:
"Add {value}" - you have to add {value} to the end of the sequence.
"Remove {value}" - you have to remove the first element in the sequence with value equal to {value}. If there is no such element you have to check if {value} is a valid index and remove the element at that index. Else you should ignore that command.
"Replace {value} {replacement}" you have to find the first occurrence of the element equal to {value} and replace its value with the {replacement}. If element equal to {value} doesn’t exists in the sequence you have to ignore this command.
"Increase {value}" you have to find the first element with value not less than {value} and increase the value of all elements in the sequence with its value. If no such element exists in the sequence, you have to take the last element from the sequence and then increase the value of all elements in the sequence with its value.
"Collapse {value}" you have to remove from the sequence every element with value less than {value}, if there are such elements.
When you receive command "Mort" you have to print the modified sequence and end the program.
Input / Constraints
•	On the first line – count of sands in each watch separated by spaces  – integers in range
[-2,147,483,648……2,147,483,647]
•	On the next lines you will receive commands untill "Mort" command is received.
•	The commands will always be valid.
Output
•	Print a single line the array of grains separated by spaces, with the modified values.
•	Allowed working time / memory: 100ms / 16MB
Examples
Input	Output	Comment
1 4 5 19 13 42 69 24
Add 1
Remove 3
Remove 4
Remove 15
Replace 0 26
Replace 1 26
Mort

26 5 13 42 69 24 1

The sequence – [1 4 5 19 13 42 69 24]
We start with "Add 1" so we add 1 to the end of the sequence –> [1 4 5 19 13 42 69 24 1]. The next command is "Remove 3" –> [1 4 5 13 42 69 24 1]. The next command is "Remove 4" –> [1 5 13 42 69 24 1]. The next command is "Remove 15" –> [1 5 13 42 69 24 1]. The next command is "Replace 0 26", neither a valid index, or such element present, so we skip this command –> [1 5 13 42 69 24 1]. The next command is "Replace 1 26" – [26 5 13 42 69 24 1]. We read "Mort" and print the sequence.

1 2 -1 0 -3 9 8 7 2
Increase 10
Increase 90
Collapse 8
Mort

8 15 14 13 8

'''

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





