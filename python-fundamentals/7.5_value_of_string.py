'''
5.	Value of a String
Write a program which finds the sum of the ASCII codes of the letters in a given string.  Your tasks will be a bit harder, because you will have to find the sum of either the lowercase or the uppercase letters.
On the first line, you will receive the string.
On the second line, you will receive one of two possible inputs:
•	If you receive "UPPERCASE"  find the sum of all uppercase English letters in the previously received string
•	 If you receive "LOWERCASE"  find the sum of all lowercase English letters in the previously received string
You should not sum the ASCII codes of any characters, which is not letters.
At the end print the sum in the following format:
•	The total sum is: {sum}
Examples
Input	                            Output
HelloFromMyAwesomePROGRAM
LOWERCASE
                                The total sum is: 1539
AC/DC
UPPERCASE	                    The total sum is: 267

'''

import re


text = input()
case = input()
if case == "LOWERCASE":
    match = re.findall('[a-z]', text)
    list_lower = []
    for letter in match:
        list_lower.append(ord(letter))
    sum_lower = sum(list_lower)
    print(f'The total sum is: {sum_lower}')

else:
    match = re.findall('[A-Z]', text)
    list_upper = []
    for letter in match:
        list_upper.append(ord(letter))
    sum_upper = sum(list_upper)
    print(f'The total sum is: {sum_upper}')
