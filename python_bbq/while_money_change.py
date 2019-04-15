s = input("Which amount of money do you want to get paid out?\n")
while True:

    # A (random) choice of bills/coins
    if s.isdigit():
        bills = [50, 20, 10, 5, 2]
        change = []
        s = int(s)
        if s > 1000000:
            print("That amount is too high - rich kid!")
        else:
            for bill in bills:
                change.append(s // bill)
                s = s % bill
            change.append(s)
    else:
        print("Funktioniert nur bei Zahlen")
        break


    print(change)
