
while True:
    try:
        m = float(input("Weight: "))
        break
    except:
        print("Weight should be numeric !")
while True:
    try:
        v = float(input("How much did you drink(in ml.): "))
        break
    except:
        print("The value should be numeric")
while True:
    gender = input("Male or Female(type M or F): ")
    if gender == "M" or gender == "F":
        break
    else:
        print("Pleas type just one letter !")
while True:
    drink = input("What kind of drink?(Type Beer/Wine/Vodka): ")
    if drink == "Beer" or drink == "Wine" or drink == "Vodka":
        break
    else:
        print("Please type just Beer/Wine/Vodka")


c = 0
a = 0
if drink == "Beer":
    a = v*0.03*0.8
elif drink == "Wine":
    a = v*0.12*0.8
elif drink == "Vodka":
    a = v*0.40*0.8


if gender == "M":
    c = a / (m*0.7)
elif gender == "F":
    c = a / (m*0.6)

print("Alcohol Concentration: {:.3}".format(c))

