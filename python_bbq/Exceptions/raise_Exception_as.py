try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise Exception("That is not a positive number!", "Get out of here!")
except Exception as ve:        # prints the error
     #print(ve)
     print(len(ve.args))