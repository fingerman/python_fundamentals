type = input()
a = input()
b = input()

def compare_int():
    int1 = int(a)
    int2 = int(b)
    if int1 > int2:
        print(str(int1))
    if int1 < int2:
        print(str(int2))
    if int1 == int2:
        print(str(int1))


def compare_char():
    if a > b:
        print(a)
    if a < b:
        print(b)
    if a == b:
        print(a)


def compare_string():
    char1 = list(a)
    char2 = list(b)

    if ord(char1[0]) > ord(char2[0]):
        print(a)
    if ord(char1[0]) < ord(char2[0]):
        print(b)
    if ord(char1[0]) == ord(char2[0]):
        print(a)


def invoke():
    if type == "int":
        compare_int()
    if type == "char":
        compare_char()
    if type == "string":
        compare_string()


invoke()



