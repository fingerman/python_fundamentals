n = int(input())
s = 0
t = 0
'''if n % 2 == 0:
    s = 2
    l = 2
else:
    s = 1
    l = 1

print((int((n - 1)/2))*"-" + s*"*" + (int((n - 1)/2))*"-")
'''

print(int((n - 1) / 2)*"-" + "*" + int((s-2))*"-" + "*" + int((n - 1) / 2)*"-")
for i in range(1, int((n + 1) / 2)):
    s += 2
    t += 1
    print((n-t)*"-" + "*" + int((s-2))*"-" + "*" + (n-t)*"-")
for i in range(1, int((n + 1) / 2)):
    s -= 2
    print(((int((n-s)/2))*"-" + "*" + (s-2)*"-" + "*" + int(((n-s)/2))*"-"))

# print((int((n - 1)/2))*"-" + l*"*" + (int((n - 1)/2))*"-")
