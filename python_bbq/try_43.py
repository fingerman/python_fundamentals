# -------------- 40 ------------

class A:
    def __init__(self):
        self.__i = 1
        self.j = 5

    def display(self):
        print(self.__i, self.j)


class B(A):
    def __init__(self):
        super().__init__()
        self.__i = 2
        self.j = 7


c = B()
print(c.__dict__)
c.display()



# ----------------------------

x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)
func()
print('Value of x is', x)

print("#---------44------------")

def say(message, times = 1):
    print(message * times)
say('Hello')
say('World', 5)


print("#------------45-------------")
total={}
def insert(items):
    if items in total:
        total[items] += 1
    else:
        total[items] = 1
insert('Apple')
insert('Ball')
insert('Apple')
print(len(total))
