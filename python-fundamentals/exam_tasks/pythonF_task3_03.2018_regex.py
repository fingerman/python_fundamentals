'''
Problem 3. Chain of Responsibility
In UnidentifiedCompany LLC, we have robot workers, who all have exactly one responsibility. The cool thing is that everyone knows someone who knows someone who is responsible for something you need done. This leads to some degree of fragmentation. In order to get anything done, you need to traverse the chain of responsibility to figure out who to ask.
You will start receiving conversation snippets containing one or more robot names, which match the following rules:
•	Begins with one or more digits
•	After that, it has one capital Latin letter, followed by one or more non-capital Latin letters
•	Ends with either a capital Latin letter or a digit, repeated two or more times.
Example valid robots: 152GoshoAAA, 1Ivan44, 43PeshoZZ
If at any point, you find a line, which has only one name in it, proceed with the following:
•	If the line ends with “!!” and has a valid name in it, you have found the manager. Print “Found the manager!: {manager_name}”
•	If it doesn’t, print “Did not find the manager!”
•	If the first name in the line isn’t the last found name from the previous line, print “Broke the chain!”
In all above cases, print the chain of responsibility on the next line, in the format: “robot1->robot2->robot3…” and end the program.
Input / Constraints
The input data should be read from the console.
•	On the first line of the input, you will receive N -  the number of lines to follow – an integer in range [2-10]
•	On the next N lines, you will receive the conversation lines, which will all be strings and each line will have at least one valid name in it.
Examples
Input
3
22IvanCC says: look for 4GoshoII
4GoshoII told me that 33Pesho11 manages that.
33Pesho11: i can help!!

Output
Found the manager!: 33Pesho11
Chain: 22IvanCC->4GoshoII->33Pesho11
-----------------------------------------------
Input
4
22IvanCC tells you to look for 1Stamat99
1Stamat99 told me 33Pesho11 is responsible.
33Pesho11 tells me to look for 1Gosho44
1Gosho44: i don't know, man

Output
Did not find the manager!
Chain: 22IvanCC->1Stamat99->33Pesho11->1Gosho44
------------------------------------------------
alternative regex:
\b\d+[A-Z][a-z]+([A-Z]|\d])\1+\b


'''


import re

name_pattern = re.compile(r'\b\d+[A-Z][a-z]+?([A-Z\d])\1+\b')

chain_of_responsibility = []

input_lines_count = int(input())
for _ in range(input_lines_count):
    line = input()

    names = list(map(lambda m: m.group(), name_pattern.finditer(line)))

    first_name, last_name = names[0], names[-1]
    print(names)
    print(first_name)
    print(last_name)

    if len(chain_of_responsibility) >= 2 and first_name != chain_of_responsibility[-1]:
        print('Broke the chain!')
        print(f'Chain: {"->".join(chain_of_responsibility)}')
        exit()

    if len(names) < 2:
        found_pattern = re.compile(name_pattern.pattern + r'.*!!$')
        responsible_match = found_pattern.match(line)

        if responsible_match:
            manager = chain_of_responsibility[-1]
            print(f'Found the manager!: {manager}')
        else:
            print('Did not find the manager!')

        print(f'Chain: {"->".join(chain_of_responsibility)}')
        exit()

    if not chain_of_responsibility:
        chain_of_responsibility.append(first_name)

    chain_of_responsibility.append(last_name)
