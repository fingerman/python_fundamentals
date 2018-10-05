'''
01. Key-Key Value-Value
Write a program, which searches for a key and value inside of several key-value pairs.
Input
•	On the first line, you will receive a key.
•	On the second line, you will receive a value.
•	On the third line, you will receive N.
•	On the next N lines, you will receive strings in the following format:
“key => {value 1};{value 2};…{value X}”
After you receive N key -> values pairs, your task is to go through them
and print only the keys, which contain the key and the values, which contain the value.
Print them in the following format:
{key}:
-{value1}
-{value2}
…
-{valueN}
Examples
Input:

bug
X
3
invalidkey => testval;x;y
debug => XUL;ccx;XC
buggy => testX;testY;XtestZ	debug:

Output:
-XUL
-XC
buggy:
-testX
-XtestZ
---------------------------
Input:
key
valu
2
xkeyc => value;value;valio
keyhole => valuable;x;values

Output:
xkeyc:
-value
-value
keyhole:
-valuable
-values

'''

key = input()
value = input()
n = int(input())
for _ in range(0, n):
    line = input()
    print(i)
