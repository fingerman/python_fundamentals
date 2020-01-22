try:
    2 / 0
except Exception as e:
    print(e)
    print(e.__str__())


#----------------
try:
    i = int("hello!")
except Exception as e:
    print(e)
    print(e.__str__())



'''
except statement is extended, and contains an additional phrase starting with the as keyword, followed by an identifier. 
The identifier is designed to catch the exception object so you can analyze its nature and draw proper conclusions.
'''