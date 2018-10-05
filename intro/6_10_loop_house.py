n = int(input())
s = 0
if n % 2 == 0:
    s = 2
    print((int((n-s)/2))*"-" + "**" + (int((n-s)/2))*"-")
else:
    s = 1
    print((int((n-s)/2))*"-" + "*" + (int((n-s)/2))*"-")
for i in range(1, int((n + 1) / 2)):
    s += 2
    print(((int((n-s)/2))*"-" + s*"*" + int(((n-s)/2))*"-"))


