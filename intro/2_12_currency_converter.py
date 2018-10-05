a = float(input())
c1 = input()
c2 = input()
if c1 == "USD" and c2 == "BGN":
    a = a * 1.79549
    print("{0:.2f}".format(a), c2)
elif c1 == "BGN" and c2 == "USD":
    a = a / 1.79549
    print("{0:.2f}".format(a), c2)
elif c1 == "BGN" and c2 == "EUR":
    a = a / 1.95583
    print("{0:.2f}".format(a), c2)
elif c1 == "EUR" and c2 == "BGN":
    a = a * 1.95583
    print("{0:.2f}".format(a), c2)
elif c1 == "BGN" and c2 == "GBP":
    a = a / 2.53405
    print("{0:.2f}".format(a), c2)
elif c1 == "GBP" and c2 == "BGN":
    a = a * 2.53405
    print("{0:.2f}".format(a), c2)
elif c1 == "USD" and c2 == "EUR":
    a = a / 1.0893
    print("{0:.2f}".format(a), c2)
elif c1 == "EUR" and c2 == "USD":
    a = a * 1.0893
    print("{0:.2f}".format(a), c2)
elif c1 == "EUR" and c2 == "GBP":
    a = a / 1.296
    print("{0:.2f}".format(a), c2)
elif c1 == "GBP" and c2 == "EUR":
    a = a * 1.296
    print("{0:.2f}".format(a), c2)










