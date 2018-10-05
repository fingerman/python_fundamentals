num = float(input())
if num <= 10:
    print("slow")
if 10 < num <= 50:
    print("average")
if 50 < num <= 150:
    print("fast")
if 150 < num <= 1000:
    print("ultra fast")
if num > 1000:
    print("extremely fast")
