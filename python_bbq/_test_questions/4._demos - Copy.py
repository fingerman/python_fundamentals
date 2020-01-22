# 1. What will be the value of the i variable when the while loop finishes its execution *

i = 0
while i != 0:
    i = i - 1
else:
    i = i + 1

print(i)
'''
a - 1
b - 2
c - 0
d - the variable will become unavailable
Answer: A
'''
#------------------------------------------
'''
3. what will be the value of the i variable when the loop finishes its execution ?
'''
for i in range(10):
    pass
print(i)
'''
a - 10
b - the variable will become unavailable
c - 11
d - 9
Answer: 9
'''
#------------------------------------------

# 4. The following expression:

print(1+-2)

# is equal to?
'''
Answ: -1
'''

#------------------------------------------
'''
5. A compiler is a program designed to?:

a - rearrange the source code to make it clearer
b - check the source code to in order to see if it is correct
c - execute the source code
d - translate the source code into machine code

(Answer: c, d)
'''
#------------------------------------------
'''
6. What is the output from the following code:
'''
a = 'ant'
b = 'bat'
c = 'came1'
print(a, b, c, sep=' ')

'''
Answer: antbatcame1
'''

#------------------------------------------
'''
7. What is the output from the following code:
'''
i = 5
while i > 0:
    i = i // 2
    if i % 2 == 0:
        break
else:
    i += 1

print(i)

# Answer: 2
# ---------------------------------
'''
8. How many lines does the code print
'''
for i in range(1, 3):
    print('*', end='')
else:
    print('*')

'''
a - one
b - three
c - two
d - four

Answer: three
'''
#------------------------------------------
'''
Scientific notation:
9. Which literal reflects the value given as 34.23

Answer: 3.42e+01
'''
# ------------------------------------------
'''
10. What is the output from the following code:
'''
a = 2
if a > 0:
    a += 1
else:
    a -= 1
print(a)

# Answer: 3
# ------------------------------------------
'''
11. Assuming the following snippet has been successfully executed. 
Which equations are True (two answers):
'''
a = [1]
b = a
a[0] = 0

print(len(a) == len(b))
print(b[0] - 1 == a[0])
print(a[0] == b[0])
print(a[0] + 1 == b[0])

'''
a.) len(a) == len(b)
b.) b[0] - 1 == a[0]
c.) a[0] == b[0]
d.) a[0] + 1 == b[0]

Answer: a, c 
'''
# ------------------------------------------
'''
12. Assuming the following snippet has been successfully executed.  
Which equations are False (two answers):
'''
a = [0]
b = a
a[0] = 1

print(len(a) == len(b))
print(b[0] - 1 == a[0])
print(a[0] == b[0])
print(a[0] + 1 == b[0])

'''
a.) len(a) == len(b)
b.) b[0] - 1 == a[0]
c.) a[0] == b[0]
d.) a[0] + 1 == b[0]

Answer: b, d 
'''
# -----------------------------------------
'''
13. Which of the following are true? Select two answers

a.) Python strings are actually lists
b.) Python strings can be concatenated
c.) Python strings can be sliced like lists
d.) Python strings are mutable

Answer: b, c ???
given - a, d
python string are immutable
'''
# ------------------------------------------
'''
Which of the following are true? Select two answers

a.) lists may not be stored inside tuples
b.) tuples may be stored inside lists
c.) tuples may not be stored inside tuples
d.) lists may be stored inside lists

Answer: b, c ???

given - c, d
'''
# ------------------------------------------
'''
15. Assuming String is six or more letters. The following slice:

String[1:-2]

is shorter from the original by how many chars?


Answer: three chars
'''
# ------------------------------------------
'''
16. What is the output from the following snippet:
'''
lst = [1, 2, 3, 4]
lst1 = lst[-3:-2]
lst2 = lst1[-1]

print(lst2)


# Answer: 2

# ---------------------------------
'''
18. How many elements will list2 contain after the execution of the following snippet
'''
list1 = [False for i in range(1,10)]
list2 = list1[-1:1:-1]
print(list2)

'''
Answer: seven
list1[-1:1:-1] # -1 is step back. if positive => None
'''
# ----------------------------
'''19. What will you use instead of XXX to check if a certain key exists in a dictionary called diet
(two ansers) '''
if XXX :
    print("Key Exists")
'''
a.) 'key' in diet
b.) diet['Pierre'] != None
c.) diet.exists('key')
d.) 'key' in diet.keys()
Answer: B,D
'''
# ----------------------------
''' 
21. Can a module run like regular code 
a.) yes, and it can differentiate its behaviour between the regular launch and import
b.) depends on Python version
c.) yes, but it cannot differentiate its behaviour between the regular launch and import
d.) no, it is not possible. A module can be imported, not run

Answer: C
'''
# ----------------------------
'''
22. Select valid fun() invocations (two answers):
'''
def fun(a, b=0):
    return a*b
'''
a.) fun(b=1)
b.) fun(a=0)
c.) fun(b=1, 0)
d.) fun(1)

Answer: b, d
'''
# ---------------------
'''
23. A file name like this one below says that (select three answers):

services.cpython-36.pyc

a.) the interpreter used to generate the file is version 3.6
b.) it has been produced by CPython
c.) it is the 36th version of the file
d.) the file comes from the services.py source file

Answer: a, b, d
'''
# ---------------------
'''
24. What is the expected behaviour of the snippet:
'''
def a(l, i):
    return l[i]

print(a([1], 0))

'''
Answer: prints 1
'''
# ---------------------
'''
25. What can you do if you have long package path to import like:
'''
import alpha.beta.gamma.delta.zeta

'''
Answer: you can make an alias for the name using the as keyword
'''
# ---------------------
'''
26. What is the expected behaviour of the snippet:
'''
string = "abcdef"

def func(s):
    del s[2]
    return s

print(func(string))

'''
Answer: -runtime error
'''
# ---------------------
'''
27. What is the expected behaviour of the snippet:
'''

def f(n):
    if n == 1:
        return '1'
    else:
        return str(n) + f(n-1)


print(f(2))

'''
a.) 21
b.) 2
c.) 3
d.) 12

Answer: a
'''
# ---------------------

'''
27. What is the expected behaviour of the snippet: *
'''

def x():            # line 1
    return 2        # line 2

x = 1 + x()         # line 3

print(x)            # line4
print(x())          # runtime exception in line 4. Integer object is not callable
'''
a.) runtime exception on line 4
b.) runtime exception on line 3
c.) runtime exception on line 1
d.) print 3

Answer: d.)
'''

# ---------------------
'''
28. What is the expected behaviour of the snippet:
'''
def f(n):
    for i in range(n + 1):
        yield i


print(f(2))
'''
a.) print 321
b.) print <generator object f at (some digits)>
c.) runtime exception
d.) print 123
Answer:
b
'''
# ---------------------
'''
29. Is it possible to safetly check if a class object has a certain attribute ?

a.) yes by using the 'hasattr' attribute
b.) yes by using the 'hasattr()' method
c.) no, it is not possible
Answer:
b.)
'''
# ---------------------
'''
30. The first argument of each class method (including init):

a.) is always a reference to the current instance of the class
b.) is always set to None
c.) is set to unique random value
d.) is set by the first argument's value

Answer:
a.)
'''
# -----------------------------
'''
33. The simplest possibe class definition in Python can be expressed as:

a.) class X
b.) class X
        pass

c.) class X
        return
d.) class X: 
        {}
        
Answer:
b)
'''
# -----------------------------
'''
34. If you want to access an exception object's components and store them in an object called e, 
you have to use the following form of exception statement

a.) except Exception(e)
b.) except e=Exception
c.) except Exception as e
d.) such an action is not possible in Python

Answer:
c.)
'''
# -----------------------------
'''
35. A variable stored separately in every object is called:
a.) there is no such variable. All (class methods) variables are shared among objects (= instances of the class)
b.) a class variable
c.) an object variable
d.) instance variable


Answer:
a.)
Class variables are static. They have the same value in all objects(class instances)
'''

# -----------------------------
'''
36. There is a stream 's' opened for writing. What option will you select to write a line to the stream

a.) s.write("Hello/n")
b.) write(s, "Hello")
c.) writeln("Hello")
d.) s.writeline("Hello")

Answer: a. ?
'''
# -----------------------------
'''

37. There is a stream 's' opened for reading. How to read one character: *

a.) ch = read(s, 1)
b.) ch = s.input(1)
c.) ch = input(s, 1)
d.) ch = s.read(1)

Answer: d 
'''
# ----------------------------
'''
38. What can you deduce from the following statement. Select two answers.
'''
str = open('file.txt', 'rt')

'''
a.) str is a string read in from the file named 'file.txt'
b.) a newline character transition will be performed during the reads
c.) if file.txt does not exists, it will be created
d.) the opened file cannot be written with the use of the str variable

Answer: A, D
'''
# ----------------------------
"""
39. The following class hierarchy is given. What is the expected output
"""
class A:
    def a(self):
        print('A', end='')

    def b(self):
        self.a()


class B(A):
    def a(self):
        print('B', end='')

    def do(self):
        self.b()


class C(A):
    def a(self):
        print('C', end='')

    def do(self):
        self.b()


B().do()
C().do()
'''
a.) BB
b.) CC
c.) AA
d.) BC
Answer:
BC 

Class B() inherits method b.a() from A(). d() calles 'b', which calls 'a' from class B() 
Similar for C()
'''
# ----------------------------
'''
40. Python built in function named open() tries to open a file and returns:

a.) an integer value identifying an opened file
b.) an error code (0 means success)
c.) a stream object
d.) always None
Answer:
C 
a corresponding file object
'''
# -----------------------------
'''
41. What is the output of the function:
'''
c = 'abc'

def x(y):
    y *= 2
    return y


z = x(c)


print(c)
'''
Answer:
abc

'''
# --------------------------------
'''
41. What is the output of the function:
'''

class A():
    def a(self):
        print("A", end='')

class B(A):
    def a(self):
        print("B", end='')


a = A()
b = B()

a.a()
b.a()
'''
Answer:
AB
'''
# ----------------
'''
(stdin) is normally connected to the keyboard, 
while the standard error and standard output go to the terminal (or window) in which you are working. 
'''
# ----------------
'''
42. What is the output of the function:
'''
i = 3
while i > 0:
    i -= 1
    if i <= 4:
        continue
else:
    print(i, end='')

'''
a.) 0
b.) 01
c.) 2
d.) error
Answer:
0
'''
# ----------------

'''
42. What is the output of the function:
'''
def ambiguous():
    return

print(ambiguous())
'''
a.) None
b.) empty line
c.) 0
d.) error
Answer:
None
'''
# ----------------
'''
42. What is the output of the function:
'''
s = '*-*'
s = s * 2 + 2 * s
print(s)

# ----------------
'''
43.) You need data which can act as a simple telephone directory. You can obtain it with the following clauses
(select two relevant variants; assume that no other items have been created before)

a.) dir = {Mom: '5551234567', Dad: '5557654321'}
b.) dir = {'Mom': '5551234567', 'Dad': '5557654321'}
c.) dir = {Mom: 5551234567, Dad: 5557654321}
d.) dir = {'Mom': 5551234567', 'Dad': 5557654321'}

print(dir)
'''
# ----------------
'''
What to youse to add an element to the end of a dictionary



a.) dict['Last'] = 49
b.) dict.append('Last', 49)
'''


# -----------------------------
'''
When you create two new class object, can they have different variables?

a.) No ....
b.) Yes if they are derived from different objects
c.) Yes, ....

Answer:
No 
'''
# -----------------------------
'''
How does a module know where he is imported at


there is a __name__() function
there is a __name__ property
???
'''
'''
The class SubClass initializes the SuperClass. How can you do that

'''


class SuperClass:

    def __init__(self, v):
        self.v = v

class Subclass(SuperClass):

    def XXX
        self.v = v

'''
a.) SuperClass.__init__(self, v)
b.) super().__init__(v)


Answer:
A, B
'''
# -----------------------------
'''
42. What is the output of the function:

'John' < 'Johnatan'

a.) True
b.) False
c.) 0
d.) 1

Answer:
A
'''
