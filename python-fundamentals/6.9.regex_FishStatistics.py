'''
Problem 09. Fish Statistics
You are a marine biologist tasked with researching various types of fish. You will receive a single line on the console as input. From this line, you must extract all the fish you find and print statistics about each one.
Fish are categorized by three criteria: tail length, body length and status. A standard fish looks like this:
><(((('>

This fish has a tail length of 1, a body length of 4 and has the status "Awake", since its eye is open. One ASCII character represents 2 centimeters in real life. By those standards, this fish has a tail length of 2 cm and a body length of 8 cm. There are various types of tails, bodies and statuses, which are described below:
•	Tail types:
o	Tail longer than 5 "<" characters  Long
o	Tail longer than 1 "<" characters  Medium
o	Tail, which is 1 "<" character long  Short
o	Nonexistent tail  None
•	Body types:
o	Body longer than 10 "(" characters  Long
o	Body longer than 5 "(" characters  Medium
o	Any other length  Short
•	Statuses:
o	'  Awake
o	-  Asleep
o	x  Dead
The input will contain a variable amount of fish, separated by any sequence of ASCII characters.
There's a possibility you might receive input, which has no fish – in this case, just print "No fish found.",
and end the program.

Input
><(((('> >>>><((((((((('>~~~~~<((->~~~  o o >>>><((x>


Output
Fish 1: ><(((('>
  Tail type: Short (2 cm)
  Body type: Short (8 cm)
  Status: Awake
Fish 2: >>>><((((((((('>
  Tail type: Medium (8 cm)
  Body type: Medium (18 cm)
  Status: Awake
Fish 3: <((->
  Tail type: None
  Body type: Short (4 cm)
  Status: Asleep
Fish 4: >>>><((x>
  Tail type: Medium (8 cm)
  Body type: Short (4 cm)
  Status: Dead
--------------------------------
Input:
            o oo     >>>><((->           * ()()()():

Fish 1: >>>><((->
  Tail type: Medium (8 cm)
  Body type: Short (4 cm)
  Status: Asleep

'''
import re


data = input()

pattern = r"(?P<tail>>*)<(?P<body>\(+)(?P<eye>['x-])>"

fish_matches = list(re.finditer(pattern, data))

for i, fish_match in enumerate(fish_matches):
    tail_len = len(fish_match.group())
    if tail_len > 5:
        tail_type = "Medium"
    # print(fish_match)
    # print(fish_match.span())
    # print(str(fish_match.group()))
    print(f'Fish:{i+1} {str(fish_match.group())}')
    print(f'  Tail type:{tail_len}')


