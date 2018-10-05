'''

32656 19759 32763 0 5 0 80 101 115 104 111 0 0 0 0 0 0 0 0 0 0 0
0 32656 19759 32763 0 7 0 83 111 102 116 117 110 105 0 0 0 0 0 0 0 0
DEBUG

Output
Pesho
Softuni


'''

import re

data = input()
pattern = r"32656 19759 32763 0 (\d+) 0 (.*?)(?= 0)"
conc_data = ''

while data != "DEBUG":
    conc_data += ' ' + data
    data = input()

enc_data = re.finditer(pattern, conc_data)
for item in enc_data:
    num = item.group(2)
    scroll_data = num.split()
    for num in scroll_data:
        num = int(num)
        print(f"{chr(num)}", end='')
    print()

'''
for match in re.finditer(pattern, conc_data):
    s = match.start()
    e = match.end()
    # print('String match "%s" at %d:%d' % (conc_data[s:e], s, e))
    print(match.group(2))
print(enc_data)
'''



'''
As a gladiator, Pesho is thrilled with ancient scrolls and is excited to have deeper understanding 
of the encoded knowledge, so he started digging. But because he can`t read the ancient computer codes, 
you should write a programm which transforms it in readable form. 
You will receive lines from the ancient memory view in 2-byte integer unsigned display.
 Each line consists of exactly 22 integers, separated by whitespace. 
 You should find every string in the whole input and print them on the console.
Every string starts with -> "32656 19759 32763"
After the pointer there is one zero and the size of the string -> "0 5"
After the size of string there is one more zero and on the next n columns are the integers for 
each character -> " 0 80 101 115 104 111" 
The above example is the string "Pesho".
You must find all strings and display them on the console, using the ASCII code for each character.
Input
•	The input will consist of a series of lines, containing 22 integers each, separated by whitespaces.
•	On the last line, you will receise the string "DEBUG"
Output
•	You should print on a new line every string you`ve found in the input in their order of appearance.

Input:
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 32656 19759 32763 0
5 0 71 111 115 104 111 0 0 0 0 0 0 0 0 0 32656 19759 32763 0 4 0
75 105 114 111 0 0 0 0 0 0 0 0 0 0 32656 19759 32763 0 8 0 86 101
114 111 110 105 107 97 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
DEBUG


Output:
Gosho
Kiro
Veronika



'''