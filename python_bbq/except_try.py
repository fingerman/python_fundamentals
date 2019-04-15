
while True:
    # try:
    #     name_input = input("Name: ")
    #     name = str(name_input)
    # except ValueError:
    #     print('The name should not be a number')
    age_input = input("Age: ")
    try:
        age = int(age_input)
    except ValueError:
        print("Type your age as integer !")

    weight = input("Input your weight in kilogram: ")
    try:
        weight = float(weight)
    except ValueError:
        print("Weight should be float !")






    print("Hi " + name + "! Your body mass index is: ", round(weight / (height * height), 2))