

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!", "Get out of here!")
except ValueError as ve:        # prints the error
     print(ve)

