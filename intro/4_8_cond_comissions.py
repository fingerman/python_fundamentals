city = input()
sales = float(input())
commission = -1

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
        result = commission*sales
        print("{0:.2f}".format(result))
    if 500 < sales <= 1000:
        commission = 0.07
        result = commission*sales
        print("{0:.2f}".format(result))
    if 1000 < sales <= 10000:
        commission = 0.08
        result = commission*sales
        print("{0:.2f}".format(result))
    if sales > 10000:
        commission = 0.12
        result = commission*sales
        print("{0:.2f}".format(result))
    if sales < 0:
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
        result = commission*sales
        print("{0:.2f}".format(result))
    if 500 < sales <= 1000:
        commission = 0.075
        result = commission*sales
        print("{0:.2f}".format(result))
    if 1000 < sales <= 10000:
        commission = 0.1
        result = commission*sales
        print("{0:.2f}".format(result))
    if sales > 10000:
        commission = 0.13
        result = commission*sales
        print("{0:.2f}".format(result))
    if sales < 0:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
        result = commission*sales
        print("{0:.2f}".format(result))
    if 500 < sales <= 1000:
        commission = 0.08
        result = commission*sales
        print("{0:.2f}".format(result))
    if 1000 < sales <= 10000:
        commission = 0.12
        result = commission*sales
        print("{0:.2f}".format(result))
    if sales > 10000:
        commission = 0.145
        result = commission*sales
        print("{0:.2f}".format(result))
    if sales < 0:
        print("error")
else:
    print("error")






