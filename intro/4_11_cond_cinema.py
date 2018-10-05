type = input()
rows = int(input())
columns = int(input())


if type == "Premiere":
    print("{0:.2f}".format(columns * rows * 12) + " leva")
elif type == "Normal":
    print("{0:.2f}".format(columns * rows * 7.50) + " leva")
elif type == "Discount":
    print("{0:.2f}".format(columns * rows * 5.00) + " leva")
else:
    print("Error")
