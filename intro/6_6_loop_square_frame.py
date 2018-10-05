n = int(input())
s = " "
print("+ " + (n-2)*"- " + "+")
for i in range(0, n-2):
    print("| "+(n-2)*"- "+"|")
print("+ " + (n-2)*"- " + "+")
