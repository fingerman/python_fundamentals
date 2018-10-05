a = int(input())
b = int(input())
c = int(input())

secs = a + b + c
mins = 0

if secs > 119:
    mins = 2
    secs = secs-120

if secs > 59:
    mins += 1
    secs = secs - 60
if secs < 10:
    print(str(mins) + ":" + "0" + str(secs))
else:
    print(str(mins) + ":" + str(secs))













































