def SignIntegerNumber(num):
    if num < 0:
        print("The number " + str(num) + " is negative.")
    if num == 0:
        print("The number " + str(num) + " is zero.")
    if num > 0:
        print("The number " + str(num) + " is positive.")

SignIntegerNumber(int(input()))
