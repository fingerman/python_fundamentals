start = int(input())
end = int(input())
step = int(input())
list = []


for i in range(start, end):
    list.append(i)

for i in list:
    if i % step == 0:
        print(i)
