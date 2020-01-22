def reciprotial(n):
    try:
        n = 1/n
    except ZeroDivisionError:
        print("Not Reciprotial")
        return None
    else:
        print("Everything went Fine")
        return n
    finally:
        print("Programm finished execution")


print(reciprotial(2))
print(reciprotial(0))

'''
code in the else clause: 
    - executed when (and only when) no exception has been raised inside the try part.
'''

